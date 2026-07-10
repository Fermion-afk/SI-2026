import Basis_operations.binary as bi
import numpy as np
import Interface.session as ss

def state_data():
    c = ss.ses["sys"]["c"]
    m = ss.ses["sys"]["n"]//2
    per = ss.ses["sys"]["per"]
    ba = ss.ses["bas"]["bas"]
    u = ss.ses["par"]["u"]
    b = ss.ses["par"]["b"]
    return c,m,per,ba,u,b

def hopp(l): #this gives the action of hopping term on bitstring of l
    _,m,per,_,_,_ = state_data()
    def even(l):  #here m denotes the number of orbitals/2
        ce = []
        for i in range((m)-1):
            x,y = bi.ca(2*i,2*i+2,l)
            if y != None:
                ce.append([x,y])     
            x1,y1 = bi.ca(2*i+2,2*i,l)
            if y1 != None:
                ce.append([x1,y1])   
        if per:
            l_u = 2*(m - 1)
            f_u = 0
            x, y = bi.ca(f_u,l_u, l)
            if y is not None:
                ce.append([x, y])
            x1, y1 = bi.ca(l_u,f_u, l)
            if y1 is not None:
                ce.append([x1, y1])
        if ce == []:
            return None
        return ce
    def odd(l): #here m denotes the number of orbitals/2
        co = []
        for i in range(m-1):
            x,y = bi.ca(2*i+1,2*i+3,l)
            if y != None:
                co.append([x,y])     
            x1,y1 = bi.ca(2*i+3,2*i+1,l)
            if y1 != None:
                co.append([x1,y1])   
        if per:
            last_dn = 2*(m - 1) + 1
            first_dn = 1
            x, y = bi.ca(first_dn, last_dn, l)
            if y is not None:
                co.append([x, y])
            x1, y1 = bi.ca(last_dn, first_dn, l)
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
    _,m,_,_,_,_ = state_data()
    k2 = 0
    for i in range(m):
        k1 = bi.nus(2*i,l)
        if k1 == 2:
            k2 += 1
    return k2

def dp(l1,l2):
    for i in l2:
        if i[1] == l1:
            return (-1)**i[0]
    return 0

def main_hub():
    c,_,_,ba,u,b = state_data()
    bas = ba
    mat1 = np.zeros((c,c))
    for i in range(c):
        for j in range(c):
            hop = hopp(bas[j])
            if i == j:
                    mat1[i][j] = hub(bas[j])*u  # diagonal
            else:
                if hop is not None:
                    mat1[i][j] = dp(bas[i], hop)*b  # off-diagonal

    return mat1









