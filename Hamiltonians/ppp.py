import config as con
import math
import Basis_operations.binary as bi
import Basis_operations.basis as basis
import numpy as np
from . import hubbard as hub

def ext(l):
    k1 = 0
    r = con.r
    for i in range(con.m-1):
        for j in range(i+1, con.m):
            vij = con.u/math.sqrt(1 + (con.u*r[i][j]/14.397)**2)
            k1 += vij*(bi.nus(2*i,l)-1)*(bi.nus(2*j,l)-1)
    return k1

def main_ppp():
    bas = con.ba
    mat1 = np.zeros((con.c, con.c))
    for i in range(con.c):
        for j in range(i, con.c):
            if i == j:
                mat1[i][j] = hub.hub(bas[j])*con.u + ext(bas[j])
            else:
                hop = hub.hopp(bas[j])
                if hop is not None:
                    val = hub.dp(bas[i], hop)*con.b
                    mat1[i][j] = val
                    mat1[j][i] = val
    return mat1

