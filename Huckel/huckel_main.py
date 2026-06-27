import math
import cmath
import numpy as np
from . import visualization as vis

def fun(N,x):
  if x == "o":
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
  elif x == "c":
    eval = []
    for i in range(N):
      eval.append(2*math.cos(2*(i)*math.pi*(1.0/N)))
    evec = []
    l = []
    for i in range(N):
      for k in range(N):
        l.append(cmath.exp(2*math.pi*1j*i*(k+1)))
      evec.append(l)
      l = []
    return eval,evec
  else :
     raise ValueError("enter either o or c")

def fun_n(m):
    m = np.array(m, dtype=int)
  
    eval, evec = np.linalg.eigh(m)
  
    eval[abs(eval) < 1e-10] = 0
    evec[abs(evec) < 1e-10] = 0
  
    return eval,evec

def hu_main():
    a = input("is the system a open chain or monocyclic(y/n):").strip().lower()
    if not(a == "y") and not(a == "n"):
        print("invalid input,enter either(y/n):")
    if a == "y":
        x = int(input("enter the number of atoms:"))
        y = input("open chain or monocyclic(o/c)").strip().lower()
        eval,evec = fun(x,y)
        b = input("visualize the orbitals(y/n):").strip().lower()
        if not(b=="y") and not(b=="n"):
            print("invalid input,enter either(y/n):")
        if b == "y":
            vis.p_o(x,y)
        elif b == "n":
            print(eval)
            print(evec)
    elif a== "n":
        n = int(input("enter the order of the adjacency matrix"))
        print("input the adjacency matrix")
        m = [] 
        for i in range(n): 
            row = input(f"Row {i+1}: ").split() 
            m.append(row)
        eval,evec = fun_n(m)
        print(eval)
        print(evec)

