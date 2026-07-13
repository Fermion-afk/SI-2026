import math
import cmath
import numpy as np
import visualization as vis

def fun(N, x):
    if x == "Open Chain":
        evals = []
        for i in range(N):
            evals.append(2*math.cos((i+1)*math.pi/(N+1)))
        evecs = []
        l = []
        for i in range(N):
            for j in range(N):
                l.append(math.sqrt(2/(N+1))*math.sin((j+1)*(i+1)*math.pi/(N+1)))
            evecs.append(l)
            l = []

    elif x == "Closed Ring":
        evals = []
        for k in range(N):
            evals.append(2*math.cos(2*math.pi*k/N))
        evecs = []
        for k in range(N):
            l = []
            for i in range(N):
                l.append(cmath.exp(2j*math.pi*i*k/N)/math.sqrt(N))
            evecs.append(l)
    else:
        raise ValueError("Enter either 'Open Chain' or 'Closed Ring'.")

    evals = np.array(evals)
    evecs = np.array(evecs)
    order = np.argsort(evals)[::-1]
    evals = evals[order]
    evecs = evecs[order]
    return evals, evecs

def fun_n(m):
    m = np.asarray(m, dtype=float)
    evals, evecs = np.linalg.eigh(m)
    evals[np.abs(evals) < 1e-10] = 0
    evecs[np.abs(evecs) < 1e-10] = 0
    return evals, evecs

def hu_main(N, per):
    evals, evecs = fun(N, per)
    while True:
        b = input("Visualize the orbitals (Yes/No): ")
        if b == "Yes":
            vis_key = "o" if per == "Open Chain" else "c"
            vis.p_o(N, vis_key, evals, evecs)
            break
        elif b == "No":
            break
        else:
            print("Invalid input. Enter either Yes or No.")
    return evals, evecs


N = int(input("Enter the number of atoms: "))
x = int(input("Is the system Open or Closed (0/1): "))

if x == 0:
    per = "Open Chain"
elif x == 1:
    per = "Closed Ring"
else:
    raise ValueError("Enter either 0 (Open Chain) or 1 (Closed Ring).")

evals, evecs = hu_main(N, per)

if N % 2 == 0:
    gap = -(evals[N//2] - evals[(N//2)-1])
else:
    gap = -(evals[(N//2)+1] - evals[N//2])

print(f"The HOMO-LUMO gap : {gap}")