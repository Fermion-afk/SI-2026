import session as ss

def parameters():

    print("="*63)
    print("                      Parameters")
    print("="*63)
    print()
    print("Current Parameters")
    print()
    print(f"On-site Energy (a)        : {ss.ses['par']['a']}")
    print(f"Hopping Parameter (b)     : {ss.ses['par']['b']}")
    print(f"On-site Repulsion (u)     : {ss.ses['par']['u']}")
    print(f"Inter-site Repulsion (v)  : {ss.ses['par']['v']}")
    print(f"Electric Field X          : {ss.ses['par']['x_f']}")
    print(f"Electric Field Y          : {ss.ses['par']['y_f']}")
    print()
    print("-"*63)
    print()
    print("1. On-site Energy")
    print("2. Hopping Parameter")
    print("3. On-site Repulsion")
    print("4. Inter-site Repulsion")
    print("5. Electric Field")
    print("6. Back")
    print()

    ch = int(input("Choice : "))
    if ch == 1:
        ss.ses["par"]["a"] = float(input("On-site Energy : "))
    elif ch == 2:
        ss.ses["par"]["b"] = float(input("Hopping Parameter : "))
    elif ch == 3:
        ss.ses["par"]["u"] = float(input("On-site Repulsion : "))
    elif ch == 4:
        ss.ses["par"]["v"] = float(input("Inter-site Repulsion : "))
    elif ch == 5:
        ss.ses["par"]["x_f"] = float(input("Electric Field X : "))
        ss.ses["par"]["y_f"] = float(input("Electric Field Y : "))
    elif ch == 6:
        return
    else:
        print("Invalid Choice")
        return
    ss.par_ready()
    ss.invalidate_ham()
    
def hamiltonian():
    print("="*63)
    print("                     Hamiltonian")
    print("="*63)
    print()
    print("Current Status")
    print()
    print(f"Basis          : {ss.ses['bas']['status']}")
    print(f"Hamiltonian    : {ss.ses['ham']['status']}")
    if ss.ses["ham"]["evecs"] == None:
        print("Eigenpairs     : Not Computed")
    else:
        print("Eigenpairs     : Ready")
    print()
    print("-"*63)
    print()
    print("1. Construct Basis")
    print("2. Construct Hamiltonian")
    print("3. Print Hamiltonian")
    print("4. Diagonalize")
    print("5. Print Eigenpairs")
    print("6. Back")
    print()
    ch = int(input("Choice : "))

    if ch == 1:
        import Basis_operations.basis as ba
        ss.ses["bas"]["bas"] = ba.binary_hash(ba.per(ss.ses["sys"]["n"],ss.ses["sys"]["k"]))
        ss.bas_ready()

    elif ch == 2:
        if ss.ses["bas"]["status"] != "Created":
            print("Construct Basis First")
            return
        def ham_creator():
            mod = ss.ses["mod"]["name"]
            if mod == "Huckel":
                import Hamiltonians.huckel as h
                ss.ses["ham"]["mat"] = h.main_huckel()
            elif mod == "Hubbard":
                import Hamiltonians.hubbard as h
                ss.ses["ham"]["mat"] = h.main_hub()
            elif mod == "Extended Hubbard":
                import Hamiltonians.ext_hubbard as h
                ss.ses["ham"]["mat"] = h.main_ext()
            elif mod == "PPP":
                import Hamiltonians.ppp as h
                ss.ses["ham"]["mat"] = h.main_ppp()
        ham_creator()
        ss.ham_ready()

    elif ch == 3:
        if ss.ses["ham"]["status"] != "Ready":
            print("Construct Hamiltonian First")
            return
        print(ss.ses["ham"]["mat"])
        
    elif ch == 4:
        if ss.ses["ham"]["status"] != "Ready":
            print("Construct Hamiltonian First")
            return
        print()
        print("1. Full")
        print("2. Lowest-k")
        print("3. Back")
        print()
        d = int(input("Choice : "))

        if d == 1:
            from numpy import linalg
            mat  = ss.ses["ham"]["mat"]
            evals,evecs = linalg.eigh(mat)
            ss.ses["ep"]["evals"] = evals 
            ss.ses["ep"]["evecs"] = evecs
            ss.ep_ready()

        elif d == 2:
            from scipy.sparse.linalg import eigsh
            mat  = ss.ses["ham"]["mat"]
            c = ss.ses["sys"]["c"]
            k = int(input(f"enter the value of k < {c}"))
            evals,evecs = eigsh(mat,k,which = "SA")
            ss.ses["ep"]["evals"] = evals 
            ss.ses["ep"]["evecs"] = evecs
            ss.ep_ready()

        elif d == 3:
             return

        else:
            print("Invalid Choice")
            return

    elif ch == 5:
        if ss.ses["ep"]["status"] != "Ready":
            print("Diagonalize the Hamiltonian first")
        evals = ss.ses["ep"]["evals"]
        k = int(input(f"Enter K for printing the lowest k eigenpairs(max:{len(evals)})"))
        print(evals[:k])
        print(ss.ses["ep"]["evecs"][:,:k])

    elif ch == 6:
        return

    else:
        print("Invalid Choice")
        return