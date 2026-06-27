import Basis_operations.basis as basis 
import Basis_operations.binary as binary 
import numpy as np
import config as con

def hopp(l): #this gives the action of hopping term on bitstring of l
    def even(l):  #here m denotes the number of orbitals/2
        ce = []
        for i in range((con.m)-1):
            l1 = []
            l2 =[]
            x,y = binary.ca(2*i,2*i+2,l)
            if y != None:
                l1.append(x)
                l1.append(y)
                ce.append(l1)     
            x1,y1 = binary.ca(2*i+2,2*i,l)
            if y1 != None:
                l2.append(x1)
                l2.append(y1)
                ce.append(l2)   
        if ce == []:
            return None
        return ce
    def odd(l): #here m denotes the number of orbitals/2
        co = []
        for i in range(con.m-1):
            l1 = []
            l2 =[]
            x,y = binary.ca(2*i+1,2*i+3,l)
            if y != None:
                l1.append(x)
                l1.append(y)
                co.append(l1)     
            x1,y1 = binary.ca(2*i+3,2*i+1,l)
            if y1 != None:
                l2.append(x1)
                l2.append(y1)
                co.append(l2)   
        if co == []:
            return None
        return co
    o = odd(l)
    e = even(l)
    if o == None and e == None:
        return None
    if o == None:
        return e
    if e == None:
        return o
    return o + e

def hub(l): # this gives the action of hubbard term on bitstring of l 
    k2 = 0
    for i in range(con.m):
        k1 = binary.nu(2*i,l)*(binary.nu(2*i+1,l))
        if k1 == 1:
            k2 += 1
    return [[k2,l]]

def dp(l1,l2):
    for i in l2:
        if i[1] == l1:
            return (-1)**i[0]
    return 0
        
def funk():
    u = basis.binary_hash(basis.per(con.n,con.k))
    mat1 = np.zeros((con.c,con.c))
    for i in range(con.c):
        for j in range(con.c):
            hop = hopp(u[j])
            if i == j:
                mat1[i][j] = hub(u[j])[0][0]*con.u  # diagonal
            else:
                if hop is not None:
                    mat1[i][j] = dp(u[i], hop)*con.b  # off-diagonal

    print(mat1)







