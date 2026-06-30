import math
import cmath
import numpy as np
from . import visualization as vis
import config as con

def fun(N,x):
  if x == "0":
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
  elif x == "1":
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

def hu_main():
    x = con.m
    y = con.x_huc
    if y == "0" or y == "1":    
        eval,evec = fun(x,y)
        b = input("visualize the orbitals(y/n):").strip().lower()
        if not(b=="y") and not(b=="n"):
            print("invalid input,enter either(y/n):")
        if b == "y":
          # visualization expects 'o' (open) or 'c' (closed);
          # map the numeric input to the expected characters
          vis_key = 'o' if y == "0" else ('c' if y == "1" else y)
          vis.p_o(x, vis_key)
        elif b == "n":
            print(eval)
            print(evec)
    elif y == "2":
        n = con.m
        print("input the adjacency matrix")
        m = [] 
        for i in range(n): 
            row = input(f"Row {i+1}: ").split() 
            m.append(row)
        eval,evec = fun_n(m)
        print(eval)
        print(evec)

