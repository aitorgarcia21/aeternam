#!/usr/bin/env python3
"""Télécharger le sous-ensemble déclaré et extraire les caractéristiques EEG avec MNE.

Les EDF restent dans donnees/brutes/ (non versionnés). Le manifeste conserve
URL, taille et SHA-256. Une nouvelle extraction vérifie les empreintes existantes.
"""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import mne
import numpy as np
import scipy

DOSSIER = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def puissances(segment, fs, bandes):
    """Périodogramme unilatéral puis intégration par bande ; entrée en volts."""
    n = segment.shape[-1]
    fenetre = np.hanning(n)
    centred = segment - segment.mean(axis=-1, keepdims=True)
    spectre = np.abs(np.fft.rfft(centred * fenetre, axis=-1)) ** 2
    spectre /= fs * np.sum(fenetre ** 2)
    spectre[:, 1:-1] *= 2  # n est pair (480) ; ni DC ni Nyquist doublés.
    f = np.fft.rfftfreq(n, 1 / fs)
    valeurs = np.stack([spectre[:, (f >= a) & (f < b)].sum(axis=-1) * fs / n
                        for a, b in bandes], axis=1)
    if not np.all(np.isfinite(valeurs)) or not np.all(valeurs > 0):
        raise ValueError('Puissances nulles ou non finies : examiner le fichier avant de poursuivre.')
    return np.log10(valeurs).ravel()


def extraire():
    p = json.loads((DOSSIER / 'protocole.json').read_text())
    donnees = DOSSIER / 'donnees'
    brutes = donnees / 'brutes'
    brutes.mkdir(parents=True, exist_ok=True)
    def telecharger(pair):
        sujet, run = pair
        nom = f'S{sujet:03d}R{run:02d}.edf'
        path = brutes / nom
        if not path.exists():
            temporaire = path.with_suffix('.edf.part')
            url = f'https://physionet.org/files/eegmmidb/1.0.0/S{sujet:03d}/{nom}'
            subprocess.run(['curl', '--fail', '--silent', '--show-error', '--location',
                            '--retry', '2', '--max-time', '180', '--output', str(temporaire), url], check=True)
            temporaire.replace(path)
        return nom
    with ThreadPoolExecutor(max_workers=4) as pool:
        for nom in pool.map(telecharger, [(s, r) for s in p['sujets'] for r in p['runs']]):
            print(f'{nom} disponible', flush=True)
    manifeste_path = donnees / 'manifest.json'
    precedent = json.loads(manifeste_path.read_text()) if manifeste_path.exists() else None
    empreintes = {f['fichier']: f['sha256'] for f in precedent['fichiers']} if precedent else {}
    fichiers, lignes = [], []
    noms = [f'{c}_{a}_{b}' for c in p['canaux'] for a, b in p['bandes_hz_demi_ouvertes']]
    for sujet in p['sujets']:
        for run in p['runs']:
            nom = f'S{sujet:03d}R{run:02d}.edf'
            url = f'https://physionet.org/files/eegmmidb/1.0.0/S{sujet:03d}/{nom}'
            path = brutes / nom
            empreinte = sha256(path)
            if nom in empreintes and empreinte != empreintes[nom]:
                raise ValueError(f'Empreinte différente pour {nom}')
            raw = mne.io.read_raw_edf(path, preload=True, verbose='ERROR')
            mne.datasets.eegbci.standardize(raw)
            fs = raw.info['sfreq']
            assert fs == p['frequence_hz_attendue'], (nom, fs)
            assert len(raw.ch_names) == 64, (nom, raw.ch_names)
            assert not raw.info['bads'], (nom, raw.info['bads'])
            data = raw.get_data(picks=p['canaux'])
            debut, fin = p['fenetre_s']
            n_essais = 0
            for ann in raw.annotations:
                label = ann['description']
                if label == 'T0':
                    continue
                assert label in p['labels'], (nom, label)
                assert ann['duration'] >= fin, (nom, ann)
                start = int(round((ann['onset'] + debut) * fs))
                stop = start + int(round((fin - debut) * fs))
                assert stop <= data.shape[-1], (nom, start, stop, data.shape)
                features = puissances(data[:, start:stop], fs, p['bandes_hz_demi_ouvertes'])
                lignes.append([sujet, run, n_essais, p['labels'][label], ann['onset'], ann['duration']]
                              + [float(x) for x in features])
                n_essais += 1
            assert n_essais > 0, nom
            fichiers.append({'fichier': nom, 'url': url, 'sha256': empreinte,
                             'octets': path.stat().st_size, 'echantillons': int(raw.n_times),
                             'frequence_hz': float(fs), 'essais': n_essais,
                             'canaux_extraits': p['canaux']})
            raw.close()
        print(f'S{sujet:03d} extrait', flush=True)
    cible = donnees / 'caracteristiques.csv'
    with cible.open('w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sujet', 'run', 'essai', 'label', 'debut_s', 'duree_s'] + noms)
        writer.writerows(lignes)
    manifeste = {
        'source': p['source'], 'licence': 'Open Data Commons Attribution License 1.0',
        'protocole_sha256': sha256(DOSSIER / 'protocole.json'),
        'versions': {'python': sys.version.split()[0], 'numpy': np.__version__,
                     'mne': mne.__version__, 'scipy': scipy.__version__},
        'fichiers': fichiers, 'caracteristiques_sha256': sha256(cible),
        'total_octets_bruts': sum(f['octets'] for f in fichiers),
        'total_essais': len(lignes), 'exclusions': [],
    }
    manifeste_path.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(lignes)} essais, {len(fichiers)} fichiers, {manifeste["total_octets_bruts"]} octets.')


if __name__ == '__main__':
    extraire()
