import os
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import Interface.session as ss
import Basis_operations.operators as op

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
        print(op.double_occ(evecs[:,st]))
    
    elif ch == 2:
        st = state_choice()
        if st == None:
            return
        print(f"x component of dipole Moment:{evals[:,st]}")
        print(f"y component of dipole Moment:{evals[:,st]}")

    elif ch == 3:
        st = state_choice()
        if st == None:
            return
        print(op.e_d(evecs[:,st]))

    elif ch == 4:
        st = state_choice()
        if st == None:
            return
        print(op.dd_corr(evecs[:,st]))

    elif ch == 5:
        return

    else:
        print("Invalid Choice")
        return
    
def sos():
    if ss.ses["ep"]["evecs"] is None:
        print("Diagonalize Hamiltonian First")
        return
    ch = select_sus()

    if ch == 1:
        st = state_choice()
        if st == None:
            return
        # Call SOS Polarizability

    elif ch == 2:
        st = state_choice()
        if st == None:
            return
        # Call SOS First Hyperpolarizability

    elif ch == 3:
        st = state_choice()
        if st == None:
            return
        # Call SOS Second Hyperpolarizability

    elif ch == 4:
        return

    else:
        print("Invalid Choice")
        return

def finite_difference():
    if ss.ses["bas"]["status"] != "Created":
        print("Construct Basis First")
        return
    ch = select_sus()

    if ch == 1:
        st = state_choice()
        if st == None:
            return
        # Call Finite Difference Polarizability

    elif ch == 2:
        st = state_choice()
        if st == None:
            return
        # Call Finite Difference First Hyperpolarizability

    elif ch == 3:
        st = state_choice()
        if st == None:
            return
        # Call Finite Difference Second Hyperpolarizability

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