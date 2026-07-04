import config as con
import math
import Basis_operations.binary as bi
import numpy as np
from . import hubbard as hub
import Basis_operations.operators as op

m_n = 1 + (con.u*con.rij/14.397)

def ext(l):
    k1 = 0
    pairs = [(i, i+1) for i in range(con.m-1)]
    if con.per:
        pairs.append((con.m-1, 0))
    for i,j in pairs:
        rij = con.r[i][j]
        ohno = math.sqrt(1 + (con.u*rij/14.397)**2)
        k1 += (con.u/ohno)*(bi.nus(2*i,l)-1)*(bi.nus(2*j,l)-1)
    return k1

def main_ext():
    bas = con.ba
    mat1 = np.zeros((con.c, con.c))
    for i in range(con.c):
        for j in range(i, con.c):
            if i == j:
                if con.run2:
                    mat1[i][j] = hub.hub(bas[j])*con.u + ext(bas[j]) + op.fi_re(con.x_f,con.y_f,bas[j])
                else: 
                    mat1[i][j] = hub.hub(bas[j])*con.u + ext(bas[j])
            else:
                hop = hub.hopp(bas[j])
                if hop is not None:
                    val = hub.dp(bas[i], hop)*(-con.b)
                    mat1[i][j] = val
                    mat1[j][i] = val
    return mat1


