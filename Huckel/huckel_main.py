import math
import cmath
import numpy as np

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
      eval.append(math.cos(2*(i)*math.pi*(1.0/N)))
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



