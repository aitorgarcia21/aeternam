#!/usr/bin/env python3
"""Calculs pédagogiques de relativité, sans données expérimentales nouvelles.

Python standard uniquement. Les valeurs PREM sont citées, pas réanalysées.
Les modèles et constantes sont décrits dans sources.md.
"""
import argparse
import json
import math
from pathlib import Path

C = 299792458.0
G = 6.67430e-11
H = 6.62607015e-34
HBAR = H / (2 * math.pi)
KB = 1.380649e-23
YEAR = 365.25 * 86400
GM_SUN = 1.3271244e20
GM_EARTH = 3.986004e14
R_EARTH = 6371000.0
G_LOCAL = 9.81  # valeur locale illustrative, pas une mesure du lieu du lecteur
M_SUN = GM_SUN / G


def addition(u, v):
    """Vitesses colinéaires en unités de c ; u est mesurée dans le mobile."""
    if not (-1 <= u <= 1 and -1 < v < 1):
        raise ValueError('u dans [-1, 1], v dans ]-1, 1[')
    return (u + v) / (1 + u * v)


def clock_static(x):
    """d tau / dt pour une horloge maintenue à r = x r_s, x > 1."""
    if x <= 1:
        raise ValueError('Une horloge statique exige r > r_s.')
    return math.sqrt(1 - 1 / x)


def clock_orbit(x):
    """Orbite circulaire géodésique stable (marginale à x = 3)."""
    if x < 3:
        raise ValueError('Orbite circulaire stable : r >= 3 r_s.')
    return math.sqrt(1 - 1.5 / x)


def phi_uniform(x):
    """Potentiel d'une sphère homogène, x = r/R, zéro à l'infini."""
    if x < 0:
        raise ValueError('Rayon négatif')
    return -GM_EARTH / R_EARTH * ((3 - x*x) / 2 if x <= 1 else 1/x)


def phi_shells(x, n=20000):
    """Vérification indépendante par somme de coquilles newtoniennes."""
    # Une coquille contribue -G dm / max(r, rayon_coquille).
    total = math.fsum(3*((i+.5)/n)**2 / max(x, (i+.5)/n) / n for i in range(n))
    return -GM_EARTH / R_EARTH * total


def black_hole(m):
    rs = 2 * G * m / C**2
    temperature = HBAR * C**3 / (8 * math.pi * G * m * KB)
    entropy = KB * 4 * math.pi * G * m*m / (HBAR * C)
    # Corps noir de surface 4 pi r_s^2 : ordre de grandeur, sans facteurs
    # de transmission, sans détail des espèces émises, sans accrétion.
    power = HBAR * C**6 / (15360 * math.pi * G*G * m*m)
    lifetime = 5120 * math.pi * G*G * m**3 / (HBAR * C**4)
    return dict(masse_kg=m, rayon_m=rs, temperature_K=temperature,
                entropie_sur_kb=entropy/KB, puissance_corps_noir_W=power,
                duree_corps_noir_ans=lifetime/YEAR)


def checks():
    # Transformer séparément dx et dt fournit un contrôle de la composition.
    errors = []
    intervals = []
    for u in [-.99, -.5, 0, .6, .99, 1]:
        for v in [-.9, 0, .8]:
            gamma = 1 / math.sqrt(1-v*v)
            dt, dx = gamma*(1+v*u), gamma*(u+v)
            errors.append(abs(dx/dt-addition(u, v)))
            intervals.append(abs(dt*dt-dx*dx-(1-u*u)))
    assert max(errors) < 1e-14 and max(intervals) < 1e-13
    shell_error = max(abs(phi_shells(x)/phi_uniform(x)-1) for x in [0, .2, .7, 1, 2])
    assert shell_error < 1e-8
    # Limite de champ faible de la solution intérieure exacte à densité constante.
    compactness = 2*GM_EARTH/(R_EARTH*C*C)
    surface_lapse = math.sqrt(1-compactness)
    centre_lapse = (3*surface_lapse-1)/2
    exact_lag = 1-centre_lapse/surface_lapse
    weak_lag = GM_EARTH/(2*R_EARTH*C*C)
    assert abs(exact_lag/weak_lag-1) < 2e-6  # soustraction de doubles proches de 1
    # Addition des rapidités, identité différente de l'expression rationnelle.
    rapidity_error = abs(addition(.9, .9)-math.tanh(2*math.atanh(.9)))
    assert rapidity_error < 1e-14
    # Première loi dE = T dS, contrôlée par différence centrée.
    m, step = M_SUN, M_SUN*1e-5
    derivative = (black_hole(m+step)['entropie_sur_kb']-
                  black_hole(m-step)['entropie_sur_kb'])*KB/(2*step)
    first_law_error = abs(black_hole(m)['temperature_K']*derivative/C**2-1)
    assert first_law_error < 1e-9
    assert math.isclose(clock_static(4/3), .5, abs_tol=1e-15)
    assert math.isclose(clock_orbit(3), 1/math.sqrt(2), rel_tol=1e-14)
    for fn, value in [(clock_static, 1), (clock_static, .5), (clock_orbit, 2)]:
        try:
            fn(value)
        except ValueError:
            pass
        else:
            raise AssertionError('Le domaine physique doit être refusé')
    return dict(statut='ok', transformation_lorentz_erreur=max(errors),
                intervalle_invariant_erreur=max(intervals), coquilles_erreur_relative=shell_error,
                interieur_exact_ecart_relatif=abs(exact_lag/weak_lag-1),
                rapidite_erreur=rapidity_error, premiere_loi_erreur_relative=first_law_error,
                domaines_invalides_refuses=True)


def calculate():
    sr = [dict(beta=b, gamma=1/math.sqrt(1-b*b),
               reference_ans=50, voyageur_ans=50*math.sqrt(1-b*b))
          for b in [.1, .5, .8, .9, .99, .999]]
    altitudes = [dict(hauteur_m=h, gain_fraction=G_LOCAL*h/C**2,
                      avance_an_s=YEAR*G_LOCAL*h/C**2,
                      avance_jour_s=86400*G_LOCAL*h/C**2)
                 for h in [.001, .01, 1, 100, 1000]]
    centre_fraction = GM_EARTH/(2*R_EARTH*C**2)
    # Relevé littéraire : eq. 12, Uggerhøj et al. (2016), PREM statique.
    prem_age_years, earth_age_years = 2.49, 4.54e9
    prem_fraction = prem_age_years/earth_age_years
    radius = [dict(r_sur_R=i/200, profondeur_km=(1-i/200)*R_EARTH/1000,
                   retard_80_ans_s=80*YEAR*centre_fraction*(1-(i/200)**2),
                   acceleration_m_s2=GM_EARTH/R_EARTH**2*(i/200))
              for i in range(201)]
    bh = [dict(r_sur_rs=x, rythme_statique=clock_static(x),
               minutes_pour_60_min_lointaines=60*clock_static(x),
               heures_lointaines_par_heure_locale=1/clock_static(x),
               rythme_orbite=clock_orbit(x) if x >= 3 else None,
               orbite_stable_possible=x >= 3)
          for x in [10, 3, 2, 4/3, 1.01, 1.0001]]
    bh_curve = [dict(r_sur_rs=x, rythme_statique=clock_static(x),
                     rythme_orbite=clock_orbit(x) if x >= 3 else None)
                for x in [1.001 + i*(8-1.001)/600 for i in range(601)]]
    return dict(
        statut='Revue critique et calculs théoriques illustratifs ; aucune nouvelle mesure.',
        date_revue='2026-10-08',
        constantes=dict(c_m_s=C, G_SI=G, h_J_s=H, kb_J_K=KB, an_julien_s=YEAR,
                        GM_solaire_nominal=GM_SUN, GM_terrestre_nominal=GM_EARTH,
                        rayon_terre_m=R_EARTH, g_local_illustratif=G_LOCAL),
        relativite_restreinte=dict(exemples=sr, addition_09_09=addition(.9,.9),
            lumiere_depuis_mobile=addition(1,.9),
            hypothese='Trajets inertiels aller-retour ; phases de manœuvre négligées.'),
        terre=dict(altitudes=altitudes, centre_homogene_fraction=centre_fraction,
            centre_homogene_80_ans_s=centre_fraction*80*YEAR,
            centre_homogene_age_ans=centre_fraction*earth_age_years,
            prem=dict(statut='Valeur publiée non réanalysée ; conversion linéaire exécutée.',
                source='https://arxiv.org/abs/1604.05507', equation=12,
                age_reference_ans=earth_age_years, retard_publie_ans=prem_age_years,
                retard_fraction=prem_fraction, retard_80_ans_s=prem_fraction*80*YEAR,
                retard_an_s=prem_fraction*YEAR),
            profil_homogene=radius,
            limites='Sphéricité et structure stationnaire ; rotation et histoire géologique omises.'),
        trou_noir=dict(exemples=bh, courbe=bh_curve,
            rayon_10_solaire_km=black_hole(10*M_SUN)['rayon_m']/1000,
            courbure_horizon_10_solaire_m_moins4=12/black_hole(10*M_SUN)['rayon_m']**4,
            limites='Schwarzschild, masse fixe, charge et rotation nulles ; référence statique à l’infini.'),
        hawking=dict(solaire=black_hole(M_SUN), dix_solaires=black_hole(10*M_SUN),
            million_solaires=black_hole(1e6*M_SUN), hypothetique_1e12kg=black_hole(1e12),
            statut='Prédiction semi-classique ; durées et puissances de corps noir simplifiées ; fin non décrite.'),
        autotests=checks())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=Path(__file__).with_name('resultats.json'))
    args = parser.parse_args()
    result = calculate()
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print('Calculs Einstein–Hawking : contrôles réussis ;', args.out)
