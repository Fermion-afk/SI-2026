from math import comb
import numpy as np
import Basis_operations.basis as bi

n = 0 #number of spin orbitals
k = 0 #number of electrons
c = 0 #dimension of occupation number space
m = 0 #number of sites or atoms
per = False #cyclic system or not
x_huc = 0

b = 1 #hopping parameter
u = 1 #intrasite repulsion parameter

rij = 1.40 #Bond length
r = np.zeros((m,m)) #Distance matrix

ba = []
    
def hu():
    global m,x_huc
    m = int(input("enter the number of atoms"))
    x_huc = input(
    """(0)linear open chain system
(1)monocylic
(2)neither""")

def hr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,ba
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    ba = bi.binary_hash(bi.per(n,k))

def ehr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,e_r,ba
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    rij = float(input("enter the bond length"))
    ba = bi.binary_hash(bi.per(n,k))
    
def p():
    global n,k,c,m,b,u,r,ba
    n = int(input("enter the number of spin orbitals: "))
    k = int(input("enter the number of electrons: "))
    c = comb(n,k)
    m = n//2
    b = float(input("enter hopping parameter: "))
    u = float(input("enter intrasite repulsion: "))
    x = input("what do you like to input a distance matrix(0) or site coordinates(1)")
    if x == "0":
        raw = input(f"enter {m}x{m} distance matrix (rows sep by ';'):")
        rows = [row.split() for row in raw.strip().split(';')]
        r = np.array([[float(x) for x in row] for row in rows])
    elif x == "1":
        coords = []
        for i in range(m):
            xy = input(f"enter x y coords for site {i} in Angstroms: ").split()
            coords.append([float(xy[0]), float(xy[1])])
        coords = np.array(coords)
        r = np.zeros((m,m))
        for i in range(m):
            for j in range(m):
                r[i][j] = np.linalg.norm(coords[i]-coords[j])
    ba = bi.binary_hash(bi.per(n,k))

