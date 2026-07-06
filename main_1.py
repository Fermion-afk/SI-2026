import config as con
from time import perf_counter as perf

run = input("Which Model Hamiltonian Would you like to Use(Huckel(hu)/Hubbard(hr)/Extended Hubbard(ehr)/PPP(p):)")

def fmt(evals, decimals=4, tol=1e-10):
    import numpy as np
    return np.where(np.abs(evals) < tol, 0.0, np.round(evals.real, decimals))

def dia(mat):
    x = input("complete spectrum(0) or lowest k eigenvalues(1)")
    if x == "1":
        import config as con
        from scipy.sparse.linalg import eigsh
        k = int(input(f"enter the value of k < {con.m}"))
        def scispa(mat,k):
            evals,evecs = eigsh(mat,k,which = "SA")
            return evals,evecs
        return scispa(mat,k)
    elif x == "0":
        from numpy import linalg
        def numdense(mat):
            evals,evecs = linalg.eigh(mat)
            return evals,evecs
        return numdense(mat)
    else:
        raise ValueError("Please enter either 0 or 1.")

def huckel():
    if con.s == 1:
        import Huckel.huckel_main as hu
        con.hu()
        hu.hu_main()
    if con.s == 0:
        import Hamiltonians.huckel as hu
        import Basis_operations.operators as op
        con.hu
        mat = hu.main_huckel()
        va,ve = dia(mat)
        x = input("Print the eigenvectors and eigenvalues(0/1):")
        if x == "1":
            print(va)
            print(ve)
        y = input("Would u like to find the double occupancy of the states(0/1)")
        if y == "1":
            y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
            print(op.expval(op.double_occ,ve[:,y_]))  
        t = input("would u like to find the dipole moment")
        if t == "1":
            y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
            print(op.expval(op.dm_x,ve[:,y_]))          
            print(op.expval(op.dm_y,ve[:,y_]))

def hubbard():
    import Hamiltonians.hubbard as hub 
    import Basis_operations.operators as op
    con.hr()
    mat = hub.main_hub()
    va,ve = dia(mat)
    x = input("Print the eigenvectors and eigenvalues(0/1):")
    if x == "1":
        print(va)
        print(ve)
    y = input("Would u like to find the double occupancy of the states(0/1)")
    if y == "1":
        y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
        print(op.expval(op.double_occ,ve[:,y_]))  
    t = input("would u like to find the dipole moment")
    if t == "1":
        y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
        print(op.expval(op.dm_x,ve[:,y_]))          
        print(op.expval(op.dm_y,ve[:,y_]))

def extended_hubbard():
    import Hamiltonians.hubbard as hub 
    import Hamiltonians.ext_hubbard as ex
    import Basis_operations.operators as op
    con.ehr()
    mat = ex.main_ext()
    va,ve = dia(mat)
    x = input("Print the eigenvectors and eigenvalues(0/1):")
    if x == "1":
        print(va)
        print(ve[:6][:])
    y = input("Would u like to find the double occupancy of the states(0/1)")
    if y == "1":
        y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
        print(op.expval(op.double_occ,ve[:,y_]))  
    t = input("would u like to find the dipole moment")
    if t == "1":
        y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
        print(op.expval(op.dm_x,ve[:,y_]))          
        print(op.expval(op.dm_y,ve[:,y_]))

def ppp():
    import Hamiltonians.hubbard as hub 
    import Hamiltonians.ppp as p 
    import Basis_operations.operators as op
    con.p()
    mat = p.main_ppp()
    va,ve = dia(mat)
    x = input("Print the eigenvectors and eigenvalues(0/1):")
    if x == "1":
        print(va)
        print(ve)
    y = input("Would u like to find the double occupancy of the states(0/1)")
    if y == "1":
        y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
        print(op.expval(op.double_occ,ve[:,y_]))  
    t = input("would u like to find the dipole moment")
    if t == "1":
        y_ = int(input("enter which state(ground->0,first excited state->1 so on...):"))
        print(op.expval(op.dm_x,ve[:,y_]))          
        print(op.expval(op.dm_y,ve[:,y_])) 
        

def ham():
    match run:
        case "hu":
            huckel()
        case "hr":
            hubbard()
        case "ehr":
            extended_hubbard()    
        case "p":
            ppp()

ham()
