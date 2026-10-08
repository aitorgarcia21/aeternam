#!/usr/bin/env python3
"""Figure descriptive issue du tableau publié, sans donnée humaine synthétique."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DOSSIER = Path(__file__).resolve().parent
r = json.loads((DOSSIER / "resultats.json").read_text())["tableau_signaux"]
rows = sorted(r["lignes"], key=lambda x: (-x["signaux"], x["ligne_source"]))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                     "text.color": "#252525", "axes.labelcolor": "#252525",
                     "xtick.color": "#252525", "ytick.color": "#252525",
                     "svg.hashsalt": "aeternam-reve-recit-v1"})
fig, ax = plt.subplots(figsize=(6.4, 5.8))
fig.subplots_adjust(left=.16, right=.91, bottom=.25, top=.80)
fig.text(.04, .955, "Répartition des signaux publiés", fontsize=19, weight="bold", va="top")
fig.text(.04, .897, "150 signaux · 13 personnes dans le tableau", fontsize=14, va="top")
y = list(range(len(rows)))
ax.barh(y, [x["signaux"] for x in rows], color="#3475a3", edgecolor="#3475a3", height=.67)
ax.set_yticks(y, [f"P{x['ligne_source']:02d}" for x in rows])
ax.invert_yaxis()
ax.set_xlim(0, 63)
ax.set_xticks([0, 20, 40, 60])
ax.set_xlabel("Nombre de signaux", labelpad=8)
ax.tick_params(axis="y", length=0, pad=8)
ax.xaxis.grid(True, color="#e3e3e3", linewidth=.7)
ax.set_axisbelow(True)
for i, row in enumerate(rows):
    ax.text(row["signaux"] + .9, i, str(row["signaux"]), va="center", fontsize=16)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color("#aaaaaa")
    ax.spines[s].set_linewidth(.7)
fig.text(.04, .065, "Source : Konkoly et al. (2026), tableau 1, p. 367.", fontsize=11)
fig.text(.04, .025, "P01–P13 : ordre des lignes source. Deux personnes sans signal.", fontsize=10)
fig.savefig(DOSSIER / "signaux-par-personne.png", dpi=170, facecolor="white")
fig.savefig(DOSSIER / "signaux-par-personne.svg", facecolor="white", metadata={"Date": None})
svg = DOSSIER / "signaux-par-personne.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
plt.close(fig)
