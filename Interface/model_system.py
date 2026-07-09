import session as ss
import numpy as np
from math import comb

m = ss.ses["sys"]["n"]//2
cords = ss.ses["sys"]["coords"]

def incords():
    cords = []
    for i in range(ss.ses["sys"]["n"]//2):
        xy = input(f"enter x y coords for site {i} in Angstroms: ").split()
        cords.append([float(xy[0]), float(xy[1])])
    cords = np.array(cords)

def dis_mat():
    r = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            r[i][j] = np.linalg.norm(cords[i]-cords[j])
    ss.ses["sys"]["dis_mat"] = r

def model():
    print("="*63)
    print("                         Model")
    print("="*63)
    print()
    print("1. Huckel")
    print("2. Hubbard")
    print("3. Extended Hubbard")
    print("4. PPP")
    print("5. Back")
    print()
    model_ch = int(input("Choice : "))
    if model_ch == 1:
        ss.ses["mod"]["name"] = "Huckel"
    elif model_ch == 2:
        ss.ses["mod"]["name"] = "Hubbard"
    elif model_ch == 3:
        ss.ses["mod"]["name"] = "Extended Hubbard"
    elif model_ch == 4:
        ss.ses["mod"]["name"] = "PPP"
    elif model_ch == 5:
        return
    else:
        print("Invalid Choice")
        input("Press Enter...")
        return
    ss.invalidate_ham()
    ss.par_ready()

def sys():

    print("="*63)
    print("                         System")
    print("="*63)
    print()
    print("Current Configuration")
    print()
    print(f"Spin Orbitals        : {ss.ses['sys']['n']}")
    print(f"Electrons            : {ss.ses['sys']['k']}")
    print(f"Boundary Condition   : {ss.ses['sys']['per']}")

    if ss.ses["sys"]["coords"] == None:
        print("Coordinates          : Not Loaded")
    else:
        print("Coordinates          : Loaded")

    print()
    print("-"*63)
    print()

    print("1. Spin Orbitals")
    print("2. Electrons")
    print("3. Boundary Condition")
    print("4. Coordinates")
    print("5. Back")
    print()

    ch = int(input("Choice : "))

    if ch == 1:
        ss.ses["sys"]["n"] = int(input("Number of Spin Orbitals : "))
        ss.sys_ready()
        ss.invalidate_bas()
        ss.invalidate_ham()

    elif ch == 2:
        ss.ses["sys"]["k"] = int(input("Number of Electrons : "))
        ss.sys_ready()
        ss.invalidate_bas()
        ss.invalidate_ham()

    elif ch == 3:
        print()
        print("1. Open Chain")
        print("2. Closed Ring")
        print("3. Neither")
        print()
        per = int(input("Choice : "))
        if per == 1:
            ss.ses["sys"]["per"] = "Open Chain"
        elif per == 2:
            ss.ses["sys"]["per"] = "Closed Ring"
        elif per == 3:
            ss.ses["sys"]["per"] = "Neither"
        else:
            print("Invalid Choice")
            input("Press Enter...")
            return
        n = ss.ses["sys"]["n"]
        k = ss.ses["sys"]["k"]
        if n != None and k != None:
            ss.ses["sys"]["c"] = comb(n,k)
        ss.sys_ready()
        ss.invalidate_ham()

    elif ch == 4:
        ss.ses["sys"]["coords"] = incords()
        cords = ss.ses["sys"]["coords"]
        ss.ses["sys"]["dis_mat"] = dis_mat()

    elif ch == 5:
        return

    else:
        print("Invalid Choice")
        input("Press Enter...")
        return