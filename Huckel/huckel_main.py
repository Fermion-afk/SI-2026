import math
import cmath
import numpy as np
from . import visualization as vis

def fun(N,x):
    if x == "Open Chain":
        eval = []
        for i in range(N):
          eval.append(2*math.cos((i+1)*math.pi*(1.0/(N+1))))
        evec = []
        l = []
        for i in range(N):
          for j in range(N):
            l.append((math.sqrt(2*(1.0/(N+1))))*math.sin((j+1)*(i+1)*math.pi*(1.0/(N+1))))
          evec.append(l)
          l = []
        return eval,evec
    elif x == "Closed Ring":
        eval = []
        for k in range(N):
            eval.append(2*math.cos(2*math.pi*k/N))
        evec = []
        for k in range(N):
            l = []
            for i in range(N):
                l.append(cmath.exp(2j*math.pi*i*k/N) / math.sqrt(N))
            evec.append(l)
        return eval, evec
    else :
        raise ValueError("enter either o or c")

def fun_n(m):
    m = np.array(m, dtype=int)
  
    eval, evec = np.linalg.eigh(m)
  
    eval[abs(eval) < 1e-10] = 0
    evec[abs(evec) < 1e-10] = 0
  
    return eval,evec

def hu_main(m,per):
    eval,evec = fun(m,per)
    while True:
        b = input("visualize the orbitals(Yes/No):")
        if b == "Yes":
            vis_key = 'o' if per == "Open Chain" else 'c' if per == "Closed Ring" else ''
            vis.p_o(m, vis_key)
            break
        elif b == "No":
            break
        else:
            print("invalid input, enter either Yes or No:")
    return eval,evec

n = int(input("Enter the number of atoms:"))
x = int(input("Is the system Open or closed(0/1)"))
per = "hello"
if x == 0:
    per = "Open Chain"
elif x == 1:
    per = "Closed Ring"
eval,evec = hu_main(n,per)
if n%2 == 0:
    print(f"The HOMO LUMO gap:{eval[(n//2)] - eval[(n//2) - 1]}")
else: 
    print(f"The HOMO LUMO gap:{eval[(n//2)+1] - eval[(n//2)]}")