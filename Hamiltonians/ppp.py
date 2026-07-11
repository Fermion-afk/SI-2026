import Interface.session as ss
import math
import Basis_operations.binary as bi
import numpy as np
from . import hubbard as hub

def state_data():
    a = ss.ses["par"]["a"]
    b = ss.ses["par"]["b"]
    u = ss.ses["par"]["u"]
    m = ss.ses["sys"]["n"]//2
    r = ss.ses["sys"]["dis_mat"]
    c = ss.ses["sys"]["c"]
    bas = ss.ses["bas"]["bas"]
    return a,b,u,m,r,c,bas

def ext(l):
    _,_,u,m,r,_,_ = state_data()
    k1 = 0
    for i in range(m-1):
        for j in range(i+1,m):
            rij = r[i][j]
            k = ss.ses["par"]["v"]
            if k == "Ohno":
                i_s = math.sqrt(1 + (u*rij/14.397)**2)
            elif k == "MN":
                i_s = 1 + (u*rij/14.397)
            else:
                raise ValueError 
            k1 += (u/i_s)*(bi.nus(2*i,l)-1)*(bi.nus(2*j,l)-1)
    return k1

def main_ppp():
    a,b,u,m,_,c,bas = state_data()
    mat1 = np.zeros((c,c))
    for i in range(c):
        for j in range(i,c):
            if i == j:
                o = 0
                for k in range(m):
                    if ss.ses["sys"]["uni"] == "Yes":
                        o += bi.nus(2*k,bas[i])*a
                    else:
                        o += bi.nus(2*k,bas[i])*a[k]
                mat1[i][j] = hub.hub(bas[j])*u + ext(bas[j]) + o
            else:
                hop = hub.hopp(bas[j])
                if hop is not None:
                    val = hub.dp(bas[i], hop)*b
                    mat1[i][j] = val
                    mat1[j][i] = val
    return mat1

