import subprocess
import sys
import re
from openpyxl import Workbook

# ===================== USER INPUTS =====================

RUN_TARGET = "main_1.py"      # <-- your main driver

MODEL = "p"                   # hu / hr / ehr / p

N_SPIN_ORBITALS = 10
N_ELECTRONS = 5
PERIODIC = 1                  # 0=open, 1=cyclic

T_HOPPING = -2
U_ONSITE = 5

FIELD_X = 1.0
FIELD_Y = 0.0

N_EXCITED = 250                # SOS cutoff

PRINT_EIGS = 0
DOUBLE_OCC = 0
DIPOLE = 0

OUTPUT_XLSX = "SOS_cyclopent.xlsx"

SITE_COORDS = [
    ( 0.0000,  1.4000),   # C1
    (-1.3315,  0.4326),   # C2
    (-0.8230, -1.1326),   # C3
    ( 0.8230, -1.1326),   # C4
    ( 1.3315,  0.4326),   # C5
]

# =======================================================

ALPHA_FACTOR = 3.57
BETA_FACTOR  = 4.997e3
GAMMA_FACTOR = 2.5695e5


def run_job():
    lines = [
        MODEL,
        str(N_SPIN_ORBITALS),
        str(N_ELECTRONS),
        str(T_HOPPING),
        str(U_ONSITE),
        str(PERIODIC),
        "1",                 # Static response = Yes
        "1",                 # SOS
    ]

    for x, y in SITE_COORDS:
        lines.append(f"{x} {y}")

    # diagonalization
    lines.append("0")        # complete spectrum

    # post diagonalization prompts
    lines.append(str(PRINT_EIGS))
    lines.append(str(DOUBLE_OCC))
    lines.append(str(DIPOLE))

    # SOS prompts
    lines.append(str(FIELD_X))
    lines.append(str(FIELD_Y))
    lines.append(str(N_EXCITED))

    proc = subprocess.run(
        [sys.executable, RUN_TARGET],
        input="\n".join(lines) + "\n",
        capture_output=True,
        text=True,
    )

    return proc.stdout, proc.stderr


def grab(name, text):
    m = re.search(rf"{name}\s*=\s*([-+0-9.eE]+)", text)
    return float(m.group(1)) if m else None


def main():
    out, err = run_job()

    print(out)

    if err.strip():
        print("stderr:")
        print(err)

    alpha = {
        "alphaxx": grab("alphaxx", out),
        "alphaxy": grab("alphaxy", out),
        "alphayy": grab("alphayy", out),
    }

    beta = {
        "betaxxx": grab("betaxxx", out),
        "betaxxy": grab("betaxxy", out),
        "betaxyy": grab("betaxyy", out),
        "betayyy": grab("betayyy", out),
    }

    gamma = {
        "gammaxxxx": grab("gammaxxxx", out),
        "gammaxxxy": grab("gammaxxxy", out),
        "gammaxxyy": grab("gammaxxyy", out),
        "gammaxyyy": grab("gammaxyyy", out),
        "gammayyyy": grab("gammayyyy", out),
    }

    wb = Workbook()
    ws = wb.active
    ws.title = "SOS_results"

    ws.append(["Parameter", "Value"])
    ws.append(["Model", MODEL])
    ws.append(["t", T_HOPPING])
    ws.append(["U", U_ONSITE])
    ws.append(["Field X", FIELD_X])
    ws.append(["Field Y", FIELD_Y])
    ws.append(["Excited states", N_EXCITED])
    ws.append([])

    ws.append(["Coordinates"])
    ws.append(["Site", "x", "y"])
    for i,(x,y) in enumerate(SITE_COORDS):
        ws.append([i,x,y])

    ws.append([])
    ws.append(["ALPHA"])
    ws.append(["Quantity","Program units","Atomic units"])

    for k,v in alpha.items():
        ws.append([k,v,None if v is None else v*ALPHA_FACTOR])

    ws.append([])
    ws.append(["BETA"])
    ws.append(["Quantity","Program units","Atomic units"])

    for k,v in beta.items():
        ws.append([k,v,None if v is None else v*BETA_FACTOR])

    ws.append([])
    ws.append(["GAMMA"])
    ws.append(["Quantity","Program units","Atomic units"])

    for k,v in gamma.items():
        ws.append([k,v,None if v is None else v*GAMMA_FACTOR])

    wb.save(OUTPUT_XLSX)
    print(f"Saved {OUTPUT_XLSX}")


if __name__ == "__main__":
    main()
