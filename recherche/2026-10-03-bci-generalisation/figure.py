#!/usr/bin/env python3
"""Figure exportable des résultats individuels ; aucune donnée inventée."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DOSSIER = Path(__file__).resolve().parent
matplotlib.rcParams['svg.hashsalt'] = 'aeternam-bci-generalisation'


def figure():
    r = json.loads((DOSSIER / 'resultats.json').read_text())
    fig, ax = plt.subplots(figsize=(3.8, 5.4), layout='constrained')
    couleur, second, texte = '#d2c29a', '#91b5ca', '#e6e1d6'
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    positions = np.arange(r['donnees']['n_personnes'])
    for nom, decalage, marque, color, label in (
        ('personne_reservee', -0.13, 'o', couleur, 'Personne inconnue'),
        ('run_reserve', 0.13, 's', second, 'Run réservé, même personne'),
    ):
        scores = [100 * v['exactitude_equilibree'] for v in r['evaluations'][nom]['par_personne']]
        ax.scatter(scores, positions + decalage, color=color, marker=marque, s=36, label=label, zorder=3)
    ax.axvline(50, color=texte, alpha=0.6, linestyle='--', linewidth=1)
    ax.set_xlim(0, 100)
    ax.set_ylim(len(positions) - 0.5, -0.5)
    ax.set_yticks(positions, [f'S{s:03d}' for s in r['protocole']['sujets']])
    ax.set_xlabel('Exactitude équilibrée (%)', color=texte, fontsize=11, labelpad=10)
    ax.tick_params(colors=texte, labelsize=11, length=0, pad=7)
    ax.grid(axis='x', color=texte, alpha=0.10)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.legend(loc='upper left', bbox_to_anchor=(0, 1.14), frameon=False,
              labelcolor=texte, fontsize=11, handletextpad=0.6)
    fig.savefig(DOSSIER / 'resultats-individuels.svg', transparent=True, metadata={'Date': None})
    fig.patch.set_alpha(1)
    fig.savefig(DOSSIER / 'resultats-individuels.png', facecolor='#0a0a0c', dpi=150)
    plt.close(fig)


if __name__ == '__main__':
    figure()
