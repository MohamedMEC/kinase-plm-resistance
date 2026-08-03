"""
Generates Figure 3 (EGFR/ABL1 forest plot) from figure3_source_data.csv.
Produces the final stacked three-panel version used in the manuscript
(figure3_egfr_abl1_forest_plot_v4.pdf/.png).

Input:  results/figure3_source_data.csv
Output: figures/figure3_egfr_abl1_forest_plot_v4.pdf, .png
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.size'] = 13
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

df = pd.read_csv('../results/figure3_source_data.csv')

groups = ['ABL1 (n=9)', 'EGFR (n=6)', 'Combined (n=15)']
predictors_key = ['ESM-1b', 'ESM-2 (150M)', 'ESM-2 (650M)', 'ESM-2 (3B)',
                   'BLOSUM62', 'Dist. to inhibitor', 'Dist. to ATP pocket']
predictors_label = ['ESM-1b', 'ESM-2-150M', 'ESM-2-650M', 'ESM-2-3B',
                     'BLOSUM62', 'Dist. to ref. ligand', 'Dist. to ATP pocket']

fig, axes = plt.subplots(3, 1, figsize=(11, 13), sharex=True)
colors = {'ABL1 (n=9)': '#2c5f8a', 'EGFR (n=6)': '#c0392b', 'Combined (n=15)': '#555555'}

for ax, grp in zip(axes, groups):
    sub = df[df['group'] == grp].set_index('predictor').loc[predictors_key]
    y = range(len(predictors_key))
    xerr_lo = sub['rho'] - sub['ci_lo']
    xerr_hi = sub['ci_hi'] - sub['rho']
    ax.errorbar(sub['rho'], y, xerr=[xerr_lo, xerr_hi], fmt='o', color=colors[grp],
                ecolor=colors[grp], elinewidth=3.5, capsize=7, capthick=3,
                markersize=13, markeredgecolor='black', markeredgewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2, linestyle='--')
    ax.set_title(grp, fontsize=18, fontweight='bold', loc='left', pad=8)
    ax.set_xlim(-1.2, 1.2)
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', length=0, labelsize=15)
    ax.grid(axis='x', linestyle=':', alpha=0.5)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    # circle markers whose 95% CI excludes zero
    for i, (lo, hi) in enumerate(zip(sub['ci_lo'], sub['ci_hi'])):
        if lo > 0 or hi < 0:
            ax.plot(sub['rho'].iloc[i], i, marker='o', mfc='none', mec='black',
                     markersize=24, markeredgewidth=2.5)
    ax.set_yticks(range(len(predictors_key)))
    ax.set_yticklabels(predictors_label)
    ax.invert_yaxis()
    for i in range(len(predictors_key)):
        ax.axhspan(i - 0.5, i + 0.5, color='#f2f2f2' if i % 2 == 0 else 'white', zorder=-1)

axes[-1].set_xlabel(r'Spearman $\rho$ (95% CI)', fontsize=16)

plt.tight_layout()
plt.savefig('../figures/figure3_egfr_abl1_forest_plot_v4.pdf', dpi=300, bbox_inches='tight')
plt.savefig('../figures/figure3_egfr_abl1_forest_plot_v4.png', dpi=150, bbox_inches='tight')
print("saved figure3_egfr_abl1_forest_plot_v4.{pdf,png}")
