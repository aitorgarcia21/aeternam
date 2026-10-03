#!/usr/bin/env python3
"""Comparer le calcul maison à deux implémentations scientifiques indépendantes."""
from __future__ import annotations

import json
from pathlib import Path

import mne
import numpy as np
from scipy.signal import periodogram
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler

from analyse import charger, plis, predire
from extraire import puissances

DOSSIER = Path(__file__).resolve().parent


def verifier():
    p, manifeste, X, y, sujets, runs = charger()
    raw = mne.io.read_raw_edf(DOSSIER / 'donnees/brutes/S001R04.edf', preload=True, verbose='ERROR')
    mne.datasets.eegbci.standardize(raw)
    fs = raw.info['sfreq']
    ann = next(a for a in raw.annotations if a['description'] in p['labels'])
    start = round((ann['onset'] + p['fenetre_s'][0]) * fs)
    stop = start + round((p['fenetre_s'][1] - p['fenetre_s'][0]) * fs)
    segment = raw.get_data(picks=p['canaux'], start=start, stop=stop)
    f, psd = periodogram(segment, fs=fs, window=np.hanning(segment.shape[-1]),
                         detrend='constant', scaling='density', axis=-1)
    reference = np.log10(np.stack([psd[:, (f >= a) & (f < b)].sum(axis=-1) * fs / segment.shape[-1]
                                  for a, b in p['bandes_hz_demi_ouvertes']], axis=1)).ravel()
    mesure = puissances(segment, fs, p['bandes_hz_demi_ouvertes'])
    assert np.allclose(mesure, reference, rtol=0, atol=1e-12)
    assert np.allclose(mesure, X[0], rtol=0, atol=1e-12)
    raw.close()
    nombre_plis = 0
    differences = 0
    for nom, folds in plis(sujets, runs).items():
        for train, test in folds:
            scaler = StandardScaler().fit(X[train])
            model = LinearDiscriminantAnalysis(solver='lsqr', shrinkage=p['regularisation'])
            model.fit(scaler.transform(X[train]), y[train])
            # La covariance de scikit-learn est pondérée par les effectifs.
            # Retirer le log des a priori empiriques pour tester nos a priori égaux.
            scores = model.decision_function(scaler.transform(X[test]))
            scores -= np.log(model.priors_[1] / model.priors_[0])
            ref = (scores > 0).astype(int)
            resultat = predire(X[train], y[train], X[test], p['regularisation'])
            differences += int(np.sum(ref != resultat))
            nombre_plis += 1
    assert differences == 0, differences
    rapport = {'spectre_max_ecart_absolu_log10': float(np.max(np.abs(mesure - reference))),
               'reference_spectrale': 'scipy.signal.periodogram, même fenêtre de Hann explicite',
               'plis_compares': nombre_plis, 'predictions_differentes': differences,
               'reference_classification': 'scikit-learn LDA lsqr shrinkage, retrait du log des a priori empiriques',
               'caracteristiques_sha256': manifeste['caracteristiques_sha256']}
    (DOSSIER / 'verification.json').write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(rapport, ensure_ascii=False))


if __name__ == '__main__':
    verifier()
