import Interface.session as ss
import math
import Basis_operations.binary as bi
import numpy as np
from . import hubbard as hub

u = ss.ses["par"]["u"]
b = ss.ses["par"]["b"]
m = ss.ses["sys"]["n"]//2
per = ss.ses["sys"]["per"]
c = ss.ses["sys"]["c"]
bas = ss.ses["bas"]["bas"]
r = ss.ses["sys"]["dis_mat"]

def ext(l):
    k1 = 0
    pairs = [(i, i+1) for i in range(m-1)]
    if per:
        pairs.append((m-1, 0))
    for i,j in pairs:
        rij = r[i][j]
        ohno = math.sqrt(1 + (u*rij/14.397)**2)
        k1 += (u/ohno)*(bi.nus(2*i,l)-1)*(bi.nus(2*j,l)-1)
    return k1

def main_ext():
    mat1 = np.zeros((c,c))
    for i in range(c):
        for j in range(i,c):
            if i == j:
                mat1[i][j] = hub.hub(bas[j])*u + ext(bas[j])
            else:
                hop = hub.hopp(bas[j])
                if hop is not None:
                    val = hub.dp(bas[i], hop)*(-b)
                    mat1[i][j] = val
                    mat1[j][i] = val
    return mat1


