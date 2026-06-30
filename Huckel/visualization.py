import math, cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import matplotlib.cm as cm
from . import huckel_main

def o_p(N):
    if N == 1: return [(0.0, 0.0)]
    return [(i, 0.0) for i in range(N)]

def c_p(N):
    pitch = 1.0
    radius = pitch * N / (2 * math.pi)
    return [(radius*math.cos(math.pi/2 - 2*math.pi*i/N),
         radius*math.sin(math.pi/2 - 2*math.pi*i/N)) for i in range(N)]

def energy_l(lam, tol=1e-6):
    if abs(lam) < tol: return r'$\alpha$'
    if abs(abs(lam)-1) < tol:
        return r'$\alpha + \beta$' if lam > 0 else r'$\alpha - \beta$'
    sign = '+' if lam > 0 else '-'
    return rf'$\alpha {sign} {abs(lam):g}\beta$'

def draw_mo(ax, coeffs, x, N):
    # accept both the single-letter codes ('o'/'c') and huckel_main's
    # numeric codes ('0' for open, '1' for closed)
    is_c = x == "c" or x == "1"
    pos  = c_p(N) if is_c else o_p(N)
    xs   = [p[0] for p in pos]; ys = [p[1] for p in pos]
    xm   = (min(xs)+max(xs))/2;  ym = (min(ys)+max(ys))/2
    npos = [(p[0]-xm, p[1]-ym) for p in pos]

    margin = 0.6
    xr = max([abs(p[0]) for p in npos] + [0.1]) + margin
    yr = max([abs(p[1]) for p in npos] + [0.1]) + margin

    for i in range(len(npos)-1):
        ax.plot([npos[i][0],npos[i+1][0]], [npos[i][1],npos[i+1][1]],
                'k-', lw=1.1, zorder=1)
    if is_c and N > 2:
        ax.plot([npos[-1][0],npos[0][0]], [npos[-1][1],npos[0][1]],
                'k-', lw=1.1, zorder=1)

    mags    = [abs(c) for c in coeffs]
    max_mag = max(mags) if max(mags) > 1e-10 else 1.0
    R       = 0.32
    hsv     = plt.get_cmap('hsv')

    for (cx,cy), coeff in zip(npos, coeffs):
        r = abs(coeff)/max_mag * R
        if r < 5e-3:
            ax.plot(cx, cy, 'ko', ms=2.5, zorder=4); continue
        if is_c:
            hue  = (cmath.phase(coeff)+math.pi)/(2*math.pi)
            color = hsv(hue)
            ax.add_patch(mpatches.Circle((cx,cy+r), r, color=color, zorder=3))
            ax.add_patch(mpatches.Circle((cx,cy-r), r, color=color, alpha=0.4, zorder=3))
        else:
            cp = '#3B82F6' if coeff >= 0 else '#F97316'
            cn = '#F97316' if coeff >= 0 else '#3B82F6'
            ax.add_patch(mpatches.Circle((cx,cy+r), r, color=cp, zorder=3))
            ax.add_patch(mpatches.Circle((cx,cy-r), r, color=cn, zorder=3))
        ax.plot(cx, cy, 'ko', ms=3, zorder=5)

    ax.set_xlim(-xr, xr); ax.set_ylim(-yr, yr)
    ax.set_aspect('equal'); ax.axis('off')

def p_o(N, x, tol=1e-6):
    fun_x = "0" if x == "o" else ("1" if x == "c" else x)
    lams, vecs = huckel_main.fun(N, fun_x)

    # ensure energies are ordered (most bonding/lowest first → most
    # antibonding/highest last), since huckel_main.fun doesn't guarantee this
    order = np.argsort(lams)[::-1]      # descending lam = ascending energy (E = α + λβ, β<0)
    lams  = [lams[k] for k in order]
    vecs  = [vecs[k] for k in order]

    # group degenerate levels (index 0 = lowest energy)
    groups, i = [], 0
    while i < N:
        lam = lams[i]; deg = 1
        while i+deg < N and abs(lams[i+deg]-lam) < tol: deg += 1
        groups.append((lam, vecs[i:i+deg])); i += deg
    n_grp   = len(groups)
    max_deg = max(len(g[1]) for g in groups)

    # figure dimensions (inches)
    spec_in = 2.5
    mo_in   = min(1.6 + 0.35 * max(0, N - 2), 4.0)     # MO column widens modestly with N, capped
    row_in  = 1.6          # per energy row
    fig_w   = spec_in + max_deg*mo_in + 0.2
    fig_h   = n_grp*row_in + 0.9

    fig = plt.figure(figsize=(fig_w, fig_h), facecolor='white')

    # spectrum axes spans full figure height (with margins)
    spec_frac_w = spec_in / fig_w
    bot_frac    = 0.07
    top_frac    = 0.93
    spec_ax = fig.add_axes((0.01, bot_frac, spec_frac_w, top_frac-bot_frac))
    spec_ax.set_xlim(0, 1)
    spec_ax.set_ylim(-0.5, n_grp-0.5)   # energy level gi sits at y=gi in data
    spec_ax.axis('off')
    spec_ax.set_title("Hückel Spectrum", fontsize=10, fontweight='bold',
                      pad=4, loc='left')

    # draw dashes + labels
    for gi, (lam, evecs) in enumerate(groups):
        deg = len(evecs)
        xs  = np.linspace(0.08, 0.50, deg) if deg > 1 else [0.29]
        for xd in xs:
            spec_ax.plot([xd-0.10, xd+0.10], [gi, gi], 'k-', lw=3)
        spec_ax.text(0.62, gi, energy_l(lam), va='center',
                     ha='left', fontsize=8.5)

    disp_to_fig = fig.transFigure.inverted()

    mo_col_frac = mo_in / fig_w
    mo_h_frac   = (row_in * 0.80) / fig_h
    left0_frac  = spec_frac_w + 0.01

    for gi, (lam, evecs) in enumerate(groups):
        deg = len(evecs)

        # get figure-fraction y of this energy level using the actual transform
        disp_pt   = spec_ax.transData.transform((0.0, gi))   # data → display
        _, y_frac = disp_to_fig.transform(disp_pt)            # display → fig frac

        total_w = deg * mo_col_frac
        x_start = left0_frac + (max_deg*mo_col_frac - total_w)/2

        for di, evec in enumerate(evecs):
            axl = x_start + di*mo_col_frac
            axb = y_frac - mo_h_frac/2
            ax  = fig.add_axes((axl, axb, mo_col_frac*0.88, mo_h_frac))
            draw_mo(ax, evec, x, N)

    # legend / colorbar
    # treat both 'o' and '0' as open-chain
    if x == "o" or x == "0":
        p1 = mpatches.Patch(color='#3B82F6', label='+ phase')
        p2 = mpatches.Patch(color='#F97316', label='− phase')
        fig.legend(handles=[p1,p2], loc='lower right',
                   fontsize=8, framealpha=0.85, ncol=2)
    else:
        sm = ScalarMappable(cmap='hsv', norm=Normalize(vmin=-math.pi, vmax=math.pi))
        sm.set_array([])
        cb_ax = fig.add_axes((0.80, 0.004, 0.16, 0.022))
        cbar  = fig.colorbar(sm, cax=cb_ax, orientation='horizontal')
        cbar.set_ticks([-math.pi, 0, math.pi])
        cbar.set_ticklabels([r'$-\pi$', '0', r'$\pi$'])
        cbar.set_label('phase', fontsize=7)
        cb_ax.tick_params(labelsize=6)

    sys_str = 'open chain' if (x == 'o' or x == '0') else 'closed ring'
    fig.suptitle(f"Hückel MO Diagram  (N={N}, {sys_str})",
                 fontsize=11, fontweight='bold', y=0.998)

    out = f"huckel_mo_N{N}_{x}.png"
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Saved → {out}")

