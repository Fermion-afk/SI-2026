from math import comb
import numpy as np
import Basis_operations.basis as bi

n = 0 #number of spin orbitals
k = 0 #number of electrons
c = 0 #dimension of occupation number space
m = 0 #number of sites or atoms
per = False #cyclic system or not
x_huc = 0
run2 = 0

b = 1 #hopping parameter
u = 1 #intrasite repulsion parameter

rij = 1.40 #Bond length
r = np.zeros((m,m)) #Distance matrix
cords = [] #system coordinates
ba = [] #basis set
x_f = 0
y_f = 0

def incords():
    global cords
    cords = []
    for i in range(m):
        xy = input(f"enter x y coords for site {i} in Angstroms: ").split()
        cords.append([float(xy[0]), float(xy[1])])
    cords = np.array(cords)
    
def hu():
    global m,x_huc,run2
    m = int(input("enter the number of atoms"))
    x_huc = input(
    """(0)linear open chain system
(1)monocylic
(2)neither""")
    run2 = int(input("Static field response(Yes:1/No:0)"))

def hr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,ba,per,run2,cords
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    per = int(input("is the system linear open chain or closed monocyclic(0/1)"))
    ba = bi.binary_hash(bi.per(n,k))
    run2 = int(input("Static field response(Yes:1/No:0)"))
    if run2:
        global x_f,y_f
        x_f = float(input("enter the x component of the field"))
        y_f = float(input("enter the y component of the field"))
        incords()

def ehr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,ba,per,r,cords,run2
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    per = int(input("is the system linear open chain or closed monocyclic(0/1)"))
    run2 = int(input("Static field response(Yes:1/No:0)"))
    if run2:
        global x_f,y_f
        x_f = float(input("enter the x component of the field"))
        y_f = float(input("enter the y component of the field"))
    incords()
    r = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            r[i][j] = np.linalg.norm(cords[i]-cords[j])
    ba = bi.binary_hash(bi.per(n,k))
    
def p():
    global n,k,c,m,b,u,r,ba,per,cords,run2
    n = int(input("enter the number of spin orbitals: "))
    k = int(input("enter the number of electrons: "))
    c = comb(n,k)
    m = n//2
    b = float(input("enter hopping parameter: "))
    u = float(input("enter intrasite repulsion: "))
    per = int(input("is the system linear open chain or closed monocyclic(0/1)"))
    run2 = int(input("Static field response(Yes:1/No:0)"))
    if run2:
        global x_f,y_f
        x_f = float(input("enter the x component of the field"))
        y_f = float(input("enter the y component of the field"))
    incords()
    r = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            r[i][j] = np.linalg.norm(cords[i]-cords[j])
    ba = bi.binary_hash(bi.per(n,k))

