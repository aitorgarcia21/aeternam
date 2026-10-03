#!/usr/bin/env python3
"""Figures scientifiques exportables depuis les résultats Monte-Carlo versionnés."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = Path(__file__).resolve().parent
matplotlib.rcParams.update({'svg.hashsalt': 'aeternam-monte-carlo-bci', 'font.family': 'DejaVu Sans'})
FG, BG = '#e6e1d6', '#0a0a0c'
OR, BLEU, GRIS = '#d2c29a', '#91b5ca', '#9a9486'


def exporter(r, nom, series):
    fig, ax = plt.subplots(figsize=(3.9, 4.5), layout='constrained')
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    x = np.array(r['protocole']['budgets_etiquetes'][1:])
    for scenario, condition, label, couleur, marque, style in series:
        c = r['scenarios'][scenario]['conditions'][condition]['gain_sur_zero_etiquette']
        y = np.array(c['moyenne'][1:])*100
        ic = np.array(c['ic_monte_carlo_95'][1:])*100
        ax.plot(x, y, label=label, color=couleur, marker=marque, markersize=4, linewidth=1.4, linestyle=style)
        ax.fill_between(x, ic[:, 0], ic[:, 1], color=couleur, alpha=.10)
    ax.axhline(0, color=GRIS, linewidth=.8)
    ax.axhline(5, color=FG, linewidth=.8, linestyle=(0, (3, 4)))
    ax.text(5, 5.18, 'Critère : +5 points', color=FG, fontsize=9)
    ax.set_xscale('log', base=2)
    ax.set_xticks(x, [str(n) for n in x])
    ax.set_ylim(-1, 10)
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.set_xlabel('Essais personnels étiquetés', fontsize=10.5, color=FG, labelpad=9)
    ax.set_ylabel('Gain sur zéro étiquette (points)', fontsize=10.5, color=FG, labelpad=8)
    ax.tick_params(colors=FG, labelsize=10, length=0, pad=6)
    ax.grid(axis='y', color=FG, alpha=.09)
    ax.spines[['top', 'right']].set_visible(False)
    for cote in ('bottom', 'left'):ax.spines[cote].set_color(GRIS)
    ax.legend(loc='lower left', bbox_to_anchor=(-.15, 1.01), fontsize=10, frameon=False, labelcolor=FG, handlelength=2.5)
    fig.savefig(D/f'{nom}.svg', transparent=True, metadata={'Date': None})
    fig.patch.set_alpha(1)
    fig.savefig(D/f'{nom}.png', facecolor=BG, dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    r = json.loads((D/'resultats.json').read_text())
    exporter(r, 'calibration-bruit', [
        ('empirique', 'bruit_ajoute', 'Bruit ajouté, sans correction', OR, 's', '-'),
        ('empirique', 'reference', 'Correction par référence', BLEU, 'o', '-'),
        ('empirique', 'niveau_initial', 'Sans bruit ajouté', GRIS, '^', '--'),
    ])
    exporter(r, 'sensibilite-modele', [
        ('empirique', 'reference', 'Contrastes ajustés aux EEG', BLEU, 'o', '-'),
        ('contraste_moitie', 'reference', 'Contrastes divisés par deux', OR, 's', '--'),
        ('derive_triple', 'reference', 'Dérive multipliée par trois', GRIS, '^', ':'),
    ])
