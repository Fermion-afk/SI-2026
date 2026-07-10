import Interface.session as ss
import numpy as np
import Hamiltonians.hubbard as hb
import Basis_operations.binary as bi

def state_data():
    n = ss.ses["sys"]["n"]
    a = ss.ses["par"]["a"]
    b = ss.ses["par"]["b"]
    c = ss.ses["par"]["c"]
    bas  = ss.ses["bas"]["bas"]
    return n,a,b,c,bas

def main_huckel():
    n,a,b,c,bas = state_data()
    mat = np.zeros((c,c))
    for i in range(c):
        for j in range(c):
            hop = hb.hopp(bas[j])
            if i == j:
                for k in range(n):
                    mat[i][j] = bi.nu(k,bas[i])*a
            else:
                if hop is not None:
                    mat[i][j] = hb.dp(bas[i], hop)*b             
    return mat

