#!/usr/bin/env python3
"""Figures de modèles physiques ; les sources ne sont pas des mesures Aeternam."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = Path(__file__).resolve().parent
FG, BG, BLUE, MUTED = '#e6e1d6', '#0a0a0c', '#91b5ca', '#9a9486'
matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'svg.hashsalt': 'aeternam-relativite-20261008'})


def canvas(title, subtitle):
    fig, ax = plt.subplots(figsize=(4.8, 4.9))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    fig.subplots_adjust(left=.18, right=.96, bottom=.19, top=.73)
    fig.text(.07, .94, title, fontsize=13, color=FG, va='top')
    fig.text(.07, .87, subtitle, fontsize=9, color=MUTED, va='top', linespacing=1.5)
    ax.tick_params(colors=FG, labelsize=10, length=3, pad=6)
    ax.spines[['top', 'right']].set_visible(False)
    for side in ['left', 'bottom']:
        ax.spines[side].set_color(MUTED)
    ax.grid(axis='y', alpha=.12, color=FG)
    ax.xaxis.label.set_color(FG)
    ax.yaxis.label.set_color(FG)
    return fig, ax


def save(fig, name):
    svg = D/f'{name}.svg'
    fig.savefig(svg, metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    fig.savefig(D/f'{name}.png', dpi=160)
    plt.close(fig)


if __name__ == '__main__':
    r = json.loads((D/'resultats.json').read_text())
    fig, ax = canvas('Horloges à l’intérieur de la Terre',
                     'Retard sur une horloge de surface après 80 ans.\nModèle sphérique stationnaire, sans rotation.')
    p = r['terre']['profil_homogene']
    ax.plot([x['r_sur_R'] for x in p], [x['retard_80_ans_s'] for x in p], color=BLUE, lw=1.8)
    val = r['terre']['prem']['retard_80_ans_s']
    ax.scatter([0], [val], s=35, marker='D', facecolors='none', edgecolors=FG, zorder=3)
    ax.annotate('PREM : valeur publiée\nconvertie sur 80 ans', (0, val), (.10, 1.34),
                fontsize=9, color=FG, va='top')
    ax.text(.12, .30, 'Sphère homogène\ncalculée ici', color=BLUE, fontsize=10)
    ax.set(xlim=(-.025,1.025), ylim=(0,1.6), ylabel='Retard accumulé (secondes)',
           xlabel='Distance au centre / rayon terrestre')
    ax.set_xticks([0,.5,1], ['0\nCentre', '0,5', '1\nSurface'])
    ax.set_yticks([0,.4,.8,1.2,1.6], ['0','0,4','0,8','1,2','1,6'])
    save(fig, 'terre-horloges')

    fig, ax = canvas('Horloges près d’un trou noir',
                     'Rapport à une horloge statique très lointaine.\nTrou noir de Schwarzschild, sans rotation.')
    p = r['trou_noir']['courbe']
    ax.plot([x['r_sur_rs'] for x in p], [x['rythme_statique'] for x in p], color=BLUE,
            lw=1.8, label='Maintien statique')
    q = [x for x in p if x['rythme_orbite'] is not None]
    ax.plot([3]+[x['r_sur_rs'] for x in q], [2**-.5]+[x['rythme_orbite'] for x in q],
            color=FG, lw=1.6, linestyle='--', label='Orbite circulaire stable')
    ax.axvline(1, color=MUTED, lw=.8, linestyle=':')
    ax.scatter([3], [2**-.5], s=28, facecolors=BG, edgecolors=FG, zorder=3)
    ax.set(xlim=(.9,8), ylim=(0,1), ylabel='Rythme local / rythme lointain',
           xlabel='Distance au centre / rayon de l’horizon')
    ax.set_xticks([1,2,3,4,6,8], ['1\nHorizon','2','3','4','6','8'])
    ax.set_yticks([0,.25,.5,.75,1], ['0','0,25','0,5','0,75','1'])
    ax.legend(loc='lower right', frameon=False, labelcolor=FG, fontsize=9)
    save(fig, 'trou-noir-horloges')
