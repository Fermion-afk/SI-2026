import config as con
import Basis_operations.basis as ba
import Basis_operations.binary as bi
import numpy as np

def dp(v1,v2): #it is expected that v1 is a hash of a vector and v2 is [n,# of vector] where n is a integer
    if v1 == v2[1]:
        return v2[0]
    else:    
        return 0

def expval(f,l): #this calculate the expectation value of "f" on the vector "vec",
    #this function assumes that "vec" is a eigenvector of "f"
    k = 0
    ba = con.ba
    m = len(l)
    for i in range(m):
        k += (np.linalg.norm(l[i])**2)*(f(ba[i]))
    return k

def expval2(l1,f,l2): #this calculate the value of f sandwiched between l1 and l2 i.e <l1|f|l2> 
    k = 0
    ba = con.ba
    m = len(l1)
    for i in range(m):
        k += l1[i]*l2[i]*(f(ba[i]))
    return k

def double_occ(evec): #give the expectation value of double occupany in a state
    k = 0
    for i in range(con.m):
        if bi.nus(2*i,evec) == 2:
            k += 1
    return k

def dm_x(l):#x component of the dipole moment
    k = 0
    for i in range(con.m):
        k += con.cords[i][0]*(bi.nus(2*i,l)-1)
    return k

def dm_y(l):#y component of the dipole moment
    k = 0
    for i in range(con.m):
        k += con.cords[i][1]*(bi.nus(2*i,l)-1)
    return k

def fi_re(x,y,l):
    k = 0 
    k += x*dm_x(l)
    k += y*dm_y(l)
    return k