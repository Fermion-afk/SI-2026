import Basis_operations.basis as basis 
import Basis_operations.binary as binary 
import numpy as np
import config as con

def hopp(l): #this gives the action of hopping term on bitstring of l
    def even(l):  #here m denotes the number of orbitals/2
        ce = []
        for i in range((con.m)-1):
            x,y = binary.ca(2*i,2*i+2,l)
            if y != None:
                ce.append([x,y])     
            x1,y1 = binary.ca(2*i+2,2*i,l)
            if y1 != None:
                ce.append([x1,y1])   
        if con.per:
            l_u = 2*(con.m - 1)
            f_u = 0
            x, y = binary.ca(f_u,l_u, l)
            if y is not None:
                ce.append([x, y])
            x1, y1 = binary.ca(l_u,f_u, l)
            if y1 is not None:
                ce.append([x1, y1])
        if ce == []:
            return None
        return ce
    def odd(l): #here m denotes the number of orbitals/2
        co = []
        for i in range(con.m-1):
            x,y = binary.ca(2*i+1,2*i+3,l)
            if y != None:
                co.append([x,y])     
            x1,y1 = binary.ca(2*i+3,2*i+1,l)
            if y1 != None:
                co.append([x1,y1])   
        if con.per:
            last_dn = 2*(con.m - 1) + 1
            first_dn = 1
            x, y = binary.ca(first_dn, last_dn, l)
            if y is not None:
                co.append([x, y])
            x1, y1 = binary.ca(last_dn, first_dn, l)
            if y1 is not None:
                co.append([x1, y1])
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
    return k2

def dp(l1,l2):
    for i in l2:
        if i[1] == l1:
            return (-1)**i[0]
    return 0
        
def main_hub():
    u = basis.binary_hash(basis.per(con.n,con.k))
    mat1 = np.zeros((con.c,con.c))
    for i in range(con.c):
        for j in range(con.c):
            hop = hopp(u[j])
            if i == j:
                mat1[i][j] = hub(u[j])*con.u  # diagonal
            else:
                if hop is not None:
                    mat1[i][j] = dp(u[i], hop)*con.b  # off-diagonal

    print(mat1)










