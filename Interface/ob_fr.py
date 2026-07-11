import os
import sys

def pause():
    input("Press Enter to continue.......")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import Interface.session as ss
import Basis_operations.operators as op
import numpy as np

def state_choice():
    print()
    print("0. Ground State")
    print("1. Excited States")
    print("2. Back")
    print()
    ch = int(input("Choice : "))
    if ch == 0:
        return 0
    elif ch == 1:
        return int(input("State Index : "))
    else:
        return None
    
def select_sus():
    print()
    print("1. Polarizability")
    print("2. First Hyperpolarizability")
    print("3. Second Hyperpolarizability")
    print("4. Back")
    print()
    return int(input("Choice : "))

def observables():
    clear()
    if ss.ses["ep"]["evecs"] is None:
        print("Diagonalize Hamiltonian First")
        return
    
    evals = ss.ses["ep"]["evals"]
    evecs = ss.ses["ep"]["evecs"]

    print("="*63)
    print("                     Observables")
    print("="*63)
    print()
    print("1. Double Occupancy")
    print("2. Dipole Moment")
    print("3. Electron Density")
    print("4. Density-Density Correlation")
    print("5. Back")
    print()
    ch = int(input("Choice : "))

    if ch == 1:
        st = state_choice()
        if st == None:
            return
        print(op.expval(op.double_occ,evecs[:,st]))
        pause()
    
    elif ch == 2:
        st = state_choice()
        if st == None:
            return
        x = op.expval(op.dm_x,evecs[:,st])
        y = op.expval(op.dm_y,evecs[:,st])
        print(f"x component of dipole Moment:{x}")
        print(f"y component of dipole Moment:{y}")
        pause()

    elif ch == 3:
        st = state_choice()
        if st == None:
            return
        print(op.e_d(evecs[:,st]))
        pause()

    elif ch == 4:
        st = state_choice()
        if st == None:
            return
        print(op.dd_corr(evecs[:,st]))
        pause()

    elif ch == 5:
        return

    else:
        print("Invalid Choice")
        pause()
        return
    
def sos():
    if ss.ses["ep"]["evecs"] is None:
        print("Diagonalize Hamiltonian First")
        pause()
        return
    ch = select_sus()

    if ch == 1:
        st = state_choice()
        if st == None:
            return
        # Call SOS Polarizability
        pause()

    elif ch == 2:
        st = state_choice()
        if st == None:
            return
        # Call SOS First Hyperpolarizability
        pause()

    elif ch == 3:
        st = state_choice()
        if st == None:
            return
        # Call SOS Second Hyperpolarizability
        pause()

    elif ch == 4:
        return

    else:
        print("Invalid Choice")
        pause()
        return

def finite_difference():
    if ss.ses["ham"]["mat"] is None:
        print("Construct the Hamiltonian First")
        pause()
        return
    
    ch = select_sus()

    def stark(x,y,i):
        c = ss.ses["sys"]["c"]
        bas = ss.ses["bas"]["bas"]
        mat = ss.ses["ham"]["mat"].copy()
        for j in range(c):
            f = x*op.dm_x(bas[j]) + y*op.dm_y(bas[j])
            mat[j,j] += f
        val,vec = np.linalg.eigh(mat)
        return val[i],vec[:,i]
    
    if ch == 1:
        st = state_choice()
        if st == None:
            return
        h = 0.04

        # x-component
        e_p, _ = stark( h, 0, st)
        e_0, _ = stark( 0, 0, st)
        e_m, _ = stark(-h, 0, st)
        alphax = -(e_p + e_m - 2*e_0)/(h*h)

        # y-component
        e_p, _ = stark(0,  h, st)
        e_0, _ = stark(0,  0, st)
        e_m, _ = stark(0, -h, st)
        alphay = -(e_p + e_m - 2*e_0)/(h*h)
        print(f"Longitudinal x component : {alphax}")
        print(f"Longitudinal y component : {alphay}")
        pause()

    elif ch == 2:
        st = state_choice()
        if st == None:
            return

        h = 0.04

        # x-component
        e_2p, _ = stark( 2*h, 0, st)
        e_p , _ = stark( h , 0, st)
        e_m , _ = stark(-h , 0, st)
        e_2m, _ = stark(-2*h, 0, st)
        betax = -(e_2p - 2*e_p + 2*e_m - e_2m)/(2*h**3)

        # y-component
        e_2p, _ = stark(0,  2*h, st)
        e_p , _ = stark(0,   h , st)
        e_m , _ = stark(0,  -h , st)
        e_2m, _ = stark(0, -2*h, st)
        betay = -(e_2p - 2*e_p + 2*e_m - e_2m)/(2*h**3)

        print(f"Longitudinal x component : {betax}")
        print(f"Longitudinal y component : {betay}")
        pause()

    elif ch == 3:
        st = state_choice()
        if st == None:
            return

        h = 0.04

        # x-component
        e_2p, _ = stark( 2*h, 0, st)
        e_p , _ = stark( h , 0, st)
        e_0 , _ = stark( 0 , 0, st)
        e_m , _ = stark(-h , 0, st)
        e_2m, _ = stark(-2*h, 0, st)
        gammax = -(e_2p - 4*e_p + 6*e_0 - 4*e_m + e_2m)/(h**4)

        # y-component
        e_2p, _ = stark(0,  2*h, st)
        e_p , _ = stark(0,   h , st)
        e_0 , _ = stark(0,   0 , st)
        e_m , _ = stark(0,  -h , st)
        e_2m, _ = stark(0, -2*h, st)
        gammay = -(e_2p - 4*e_p + 6*e_0 - 4*e_m + e_2m)/(h**4)

        print(f"Longitudinal x component : {gammax}")
        print(f"Longitudinal y component : {gammay}")
        pause()

    elif ch == 4:
        return

    else:
        print("Invalid Choice")
        return

def finite_field():
    while True:
        clear()
        print("="*63)
        print("                Finite Field Response")
        print("="*63)
        print()
        print("1. Sum Over States")
        print("2. Finite Difference")
        print("3. Back")
        print()
        ch = int(input("Choice : "))

        if ch == 1:
            sos()

        elif ch == 2:
            finite_difference()

        elif ch == 3:
            return

        else:
            print("Invalid Choice")
            return