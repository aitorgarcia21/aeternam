#!/usr/bin/env python3
"""Campagnes virtuelles de calibration BCI, calées sur six caractéristiques EEG.

NumPy seulement. Les tirages de calibration, de test, des profils sources et de
référence sont indépendants. Les scénarios et budgets partagent leurs aléas pour
des comparaisons appariées. Les paramètres du générateur ne sont jamais fournis
au décodeur. Les intervalles sont conditionnels au générateur fixé.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import numpy as np

DOSSIER = Path(__file__).resolve().parent


def empreinte(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cov_reg(cov, coefficient):
    return (1-coefficient)*cov + coefficient*np.diag(np.maximum(np.diag(cov), 1e-8))


def statistiques(X, y):
    moyennes = np.stack([X[y == c].mean(0) for c in (0, 1)])
    residus = X-moyennes[y]
    return moyennes, residus.T @ residus / (len(X)-2)


def ajuster_profil(X, y, runs, retrait):
    moyennes, _ = statistiques(X, y)
    residus, centres, variances_moyenne = [], [], []
    for run in np.unique(runs):
        idx = runs == run
        m = np.stack([X[idx & (y == c)].mean(0) for c in (0, 1)])
        residus.append(X[idx]-m[y[idx]])
        centres.append(m.mean(0))
        variances_moyenne.append(sum(1/np.sum(idx & (y == c)) for c in (0, 1))/4)
    e = np.vstack(residus)
    covariance = cov_reg(e.T @ e/(len(X)-2*len(centres)), retrait)
    variance_derive = np.maximum(np.var(centres, axis=0, ddof=1)
                                - np.diag(covariance)*np.mean(variances_moyenne), 0)
    return {'centre': moyennes.mean(0), 'contraste': moyennes[1]-moyennes[0],
            'covariance': covariance, 'ecart_derive': np.sqrt(variance_derive)}


def charger(p):
    path = (DOSSIER/p['source']).resolve()
    assert empreinte(path) == p['source_sha256']
    with path.open(newline='') as f:
        lignes = list(csv.DictReader(f))
    noms = [k for k in lignes[0] if k.startswith(('C3_', 'Cz_', 'C4_'))]
    X = np.array([[float(l[k]) for k in noms] for l in lignes])
    y = np.array([int(l['label']) for l in lignes])
    sujets = np.array([int(l['sujet']) for l in lignes])
    runs = np.array([int(l['run']) for l in lignes])
    centre, echelle = X.mean(0), X.std(0)
    X = (X-centre)/echelle  # Unités du générateur, pas apprentissage sur un test virtuel.
    profils = [ajuster_profil(X[sujets == s], y[sujets == s], runs[sujets == s],
                              p['covariance_generatrice_retrait_diagonal'])
               for s in np.unique(sujets)]
    return profils, {'personnes_reelles': len(profils), 'essais_reels': len(X),
                     'caracteristiques': noms, 'centre_unites': centre.tolist(),
                     'echelle_unites': echelle.tolist(), 'sha256': empreinte(path)}, (X, y, sujets, runs)


def etiquettes(n):
    assert n % 2 == 0
    return np.arange(n) % 2


def mesures(profil, n, rng, contraste, derive):
    y = etiquettes(n)
    offset = rng.normal(size=6)*profil['ecart_derive']*derive
    signal = (profil['centre'] + offset
              + (y[:, None]-.5)*profil['contraste']*contraste)
    return signal + rng.normal(size=(n, 6)) @ np.linalg.cholesky(profil['covariance']).T, y


def adapter(source_stats, X, y, p, personnel_seul=False):
    if len(X) == 0:
        return source_stats
    mu_s, cov_s = source_stats
    mu_t, cov_t = statistiques(X, y)
    poids = 1.0 if personnel_seul else len(X)/(len(X)+p['poids_a_priori_en_essais'])
    return (1-poids)*mu_s+poids*mu_t, (1-poids)*cov_s+poids*cov_t


def predire(stats, X, retrait):
    mu, cov = stats
    poids = np.linalg.solve(cov_reg(cov, retrait), mu[1]-mu[0])
    return ((X-.5*(mu[0]+mu[1])) @ poids > 0).astype(int)


def ajuster_reference(R, X, ridge):
    R0, X0 = R.mean(0), X.mean(0)
    A, B = R-R0, X-X0
    coeff = np.linalg.solve(A.T@A/len(A)+ridge*np.eye(R.shape[1]), A.T@B/len(A))
    return coeff, R0


def bruiter(cal, test, profil, rng, p):
    # Deux perturbations communes : canaux de la première et de la seconde bande.
    B = np.zeros((2, 6))
    B[0, ::2] = B[1, 1::2] = 1/math.sqrt(3)
    n_bg = p['observations_reference_non_etiquetees']
    n = len(cal)+len(test)
    clean = np.vstack([cal, test])
    z = rng.normal(size=(n, 2))*p['bruit_supplementaire_ecart_type']
    eta = rng.normal(size=(n, 2))*p['erreur_capteur_reference_ecart_type']
    z_bg = rng.normal(size=(n_bg, 2))*p['bruit_supplementaire_ecart_type']
    eta_bg = rng.normal(size=(n_bg, 2))*p['erreur_capteur_reference_ecart_type']
    neural_bg = rng.normal(size=(n_bg, 6)) @ np.linalg.cholesky(profil['covariance']).T
    observed_bg = neural_bg + z_bg@B
    observed = clean + z@B
    retour = {'niveau_initial': clean, 'bruit_ajoute': observed,
              'attenuation': clean+p['amplitude_residuelle_scenario_attenuation']*z@B}
    for nom, fuite in [('reference', 0), ('reference_contaminee', p['fuite_vers_reference_scenario_stress'])]:
        R_bg = z_bg+eta_bg+fuite*neural_bg@B.T
        R = z+eta+fuite*(clean-profil['centre'])@B.T
        coeff, centre = ajuster_reference(R_bg, observed_bg, p['ridge_reference'])
        retour[nom] = observed-(R-centre)@coeff
    return {k: (v[:len(cal)], v[len(cal):], float(np.mean((v[len(cal):]-test)**2)))
            for k, v in retour.items()}


def resumer(scores):
    a = np.asarray(scores)
    moyenne = a.mean(0)
    demi = 1.96*a.std(0, ddof=1)/math.sqrt(len(a))
    return {'moyenne': moyenne.tolist(), 'ic_monte_carlo_95': np.stack([moyenne-demi, moyenne+demi], -1).tolist(),
            'quantiles_campagnes_10_90': np.quantile(a, [.1, .9], axis=0).T.tolist()}


def seuil_gain(resume, budgets, minimum):
    mu = np.asarray(resume['moyenne'])
    ic = np.asarray(resume['ic_monte_carlo_95'])
    valide = (100*mu >= minimum) & (ic[:, 0] > 0)
    for i, n in enumerate(budgets):
        if n and np.all(valide[i:]):
            return n
    return None


def diagnostic_humain(data, retrait):
    """Contrôle descriptif hors run du générateur gaussien ; pas un réglage."""
    X, y, sujets, runs = data
    distances = []
    for s in np.unique(sujets):
        for run in np.unique(runs):
            train = (sujets == s) & (runs != run)
            test = (sujets == s) & (runs == run)
            mu, cov = statistiques(X[train], y[train])
            cov = cov_reg(cov, retrait)
            for c in (0, 1):
                e = X[test & (y == c)]-mu[c]
                predictive = cov*(1+1/np.sum(train & (y == c)))
                distances.extend(np.einsum('ij,ij->i', e@np.linalg.inv(predictive), e).tolist())
    # Quantile 95 % du chi-deux à 6 ddl, calculé depuis sa CDF exacte.
    lo, hi = 0., 100.
    for _ in range(80):
        mid = (lo+hi)/2
        cdf = 1-math.exp(-mid/2)*(1+mid/2+(mid/2)**2/2)
        if cdf < .95: lo = mid
        else: hi = mid
    seuil = (lo+hi)/2
    return {'n': len(distances), 'couverture_ellipse_gaussienne_indicative_95': float(np.mean(np.array(distances) <= seuil)),
            'seuil_chi2_6': seuil,
            'limite': 'Diagnostic de transport entre runs ; référence indicative, covariance et moyennes estimées. Ce n’est pas un test exact ni une validation clinique.'}


def autotests():
    rng = np.random.default_rng(170)
    # Un capteur indépendant et exact permet de retirer un mélange connu.
    R = rng.normal(size=(256, 2))
    B = rng.normal(size=(2, 6))
    coeff, _ = ajuster_reference(R, R@B, 0)
    assert np.allclose(coeff, B, atol=1e-12)
    # La suppression peut aussi retirer un signal utile capté par la référence.
    signal = rng.normal(size=(256, 1))
    coeff, centre = ajuster_reference(signal, signal, 0)
    assert np.var(signal-(signal-centre)@coeff) < 1e-20
    # Générateur gaussien : comparer le meilleur décodeur connu à sa probabilité analytique.
    profil = {'centre': np.zeros(6), 'contraste': np.array([1., 0, 0, 0, 0, 0]),
              'covariance': np.eye(6), 'ecart_derive': np.zeros(6)}
    X, y = mesures(profil, 100000, rng, 1, 0)
    score = np.mean((X[:, 0] > 0) == y)
    attendu = .5*(1+math.erf(.5/math.sqrt(2)))
    assert abs(score-attendu) < .005
    # Un test supplémentaire ne doit pas modifier l’entraînement ou les autres prédictions.
    stats = statistiques(X[:100], y[:100])
    first = predire(stats, X[100:120], .1)
    assert np.array_equal(first, predire(stats, np.vstack([X[100:120], np.ones(6)*1e10]), .1)[:20])
    return {'gaussien_score': float(score), 'gaussien_probabilite_analytique': attendu,
            'regression_reference_exacte': True, 'risque_retrait_signal_verifie': True,
            'test_sans_influence_sur_apprentissage': True}


def analyser():
    p = json.loads((DOSSIER/'protocole.json').read_text())
    controles = autotests()
    profils, origine, data = charger(p)
    resultats = {}
    for scenario in p['scenarios']:
        scores = {k: [] for k in p['conditions']}
        solo = {k: [] for k in p['conditions']}
        erreurs = {k: [] for k in p['conditions']}
        indexes = []
        for iteration in range(p['repetitions']):
            # Réinitialisation voulue : mêmes aléas entre scénarios, nouveaux aléas entre campagnes.
            rng = np.random.default_rng(np.random.SeedSequence([p['graine'], iteration]))
            k = int(rng.integers(len(profils)))
            indexes.append(k+1)
            sources = [mesures(profil, p['essais_source_par_profil'], rng, scenario['contraste'], scenario['derive'])
                       for j, profil in enumerate(profils) if j != k]
            stats = statistiques(np.vstack([x for x, _ in sources]), np.concatenate([y for _, y in sources]))
            cal, y_cal = mesures(profils[k], max(p['budgets_etiquetes']), rng, scenario['contraste'], scenario['derive'])
            test, y_test = mesures(profils[k], p['essais_test_independants'], rng, scenario['contraste'], scenario['derive'])
            conditions = bruiter(cal, test, profils[k], rng, p)
            for nom in p['conditions']:
                C, T, erreur = conditions[nom]
                courbe, courbe_solo = [], []
                for n in p['budgets_etiquetes']:
                    modele = adapter(stats, C[:n], y_cal[:n], p)
                    courbe.append(float(np.mean(predire(modele, T, p['covariance_decodeur_retrait_diagonal']) == y_test)))
                    if n:
                        seul = adapter(stats, C[:n], y_cal[:n], p, personnel_seul=True)
                        courbe_solo.append(float(np.mean(predire(seul, T, p['covariance_decodeur_retrait_diagonal']) == y_test)))
                scores[nom].append(courbe)
                solo[nom].append(courbe_solo)
                erreurs[nom].append(erreur)
        conditions = {}
        for nom in p['conditions']:
            a = np.array(scores[nom])
            gain = resumer(a-a[:, :1])
            versus_bruit = resumer(a-np.array(scores['bruit_ajoute']))
            conditions[nom] = {'scores': resumer(a), 'gain_sur_zero_etiquette': gain,
                               'gain_sur_bruit_non_corrige': versus_bruit,
                               'personnel_seul': resumer(solo[nom]),
                               'minimum_budget_gain': seuil_gain(gain, p['budgets_etiquetes'], p['gain_minimal_points']),
                               'erreur_sur_mesure_initiale_moyenne': float(np.mean(erreurs[nom])),
                               'scores_par_campagne': scores[nom], 'personnel_seul_par_campagne': solo[nom]}
        resultats[scenario['cle']] = {'profils_par_campagne': indexes, 'conditions': conditions}
        print(f"Scénario {scenario['cle']} terminé", flush=True)
    nul = resultats['nul']['conditions']
    controles['nul_max_ecart_a_50'] = max(abs(v-.5) for c in nul.values() for v in c['scores']['moyenne'])
    assert controles['nul_max_ecart_a_50'] < .015
    return {'statut': p['statut'], 'protocole': p, 'protocole_sha256': empreinte(DOSSIER/'protocole.json'),
            'origine': origine, 'controles': controles, 'diagnostic_humain': diagnostic_humain(data, p['covariance_generatrice_retrait_diagonal']),
            'parametres_profils': [{k: v.tolist() for k, v in profil.items()} for profil in profils],
            'scenarios': resultats}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DOSSIER/'resultats.json')
    args = parser.parse_args()
    resultat = analyser()
    args.out.write_text(json.dumps(resultat, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'origine': resultat['origine'], 'controles': resultat['controles'],
                      'diagnostic_humain': resultat['diagnostic_humain'],
                      'seuils': {s: {c: r['minimum_budget_gain'] for c, r in v['conditions'].items()}
                                  for s, v in resultat['scenarios'].items()}}, ensure_ascii=False))
