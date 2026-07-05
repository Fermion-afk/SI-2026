import numpy as np
import config as con
from time import perf_counter as perf

run = input("Which Model Hamiltonian Would you like to Use(Huckel(hu)/Hubbard(hr)/Extended Hubbard(ehr)/PPP(p):)")

def fmt(evals, decimals=4, tol=1e-10):
    return np.where(np.abs(evals) < tol, 0.0, np.round(evals.real, decimals))

def ham():
    match run:
        case "hu":
            import Huckel.huckel_main as hu
            con.hu()
            hu.hu_main()

        case "hr":
            import Hamiltonians.hubbard as hub 
            import Basis_operations.diagonalization as di
            import Basis_operations.operators as op
            con.hr()
            mat = hub.main_hub()
            va,ve = di.scispa(mat)
            x = input("Print the eigenvectors and eigenvalues(0/1):")
            if x == "1":
                print(va)
                print(ve)
            y = input("Would u like to find the double occupancy of the states(0/1)")
            if y == "1":
                y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
                print(op.expval(op.double_occ,ve[:,y_]))  
            
        case "ehr":
            import Hamiltonians.hubbard as hub 
            import Hamiltonians.ext_hubbard as ex
            import Basis_operations.diagonalization as di
            import Basis_operations.operators as op
            con.ehr()
            mat = ex.main_ext()
            va,ve = di.scispa(mat)
            x = input("Print the eigenvectors and eigenvalues(0/1):")
            if x == "1":
                print(va)
                print(ve[:6][:])
            
        case "p":
            import Hamiltonians.hubbard as hub 
            import Hamiltonians.ppp as p 
            import Basis_operations.diagonalization as di
            import Basis_operations.operators as op
            con.p()
            mat = p.main_ppp()
            va,ve = di.scispa(mat)
            x = input("Print the eigenvectors and eigenvalues(0/1):")
            if x == "1":
                print(va)
                print(ve)

ham()