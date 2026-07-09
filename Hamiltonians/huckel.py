import Interface.session as ss
import numpy as np
import Hamiltonians.hubbard as hb
import Basis_operations.binary as bi

a = ss.ses["sys"]["a"]
b = ss.ses["sys"]["b"]
c = ss.ses["sys"]["c"]
bas  = ss.ses["bas"]["bas"]

def main_huckel():
    mat = np.zeros((c,c))
    for i in range(c):
        for j in range(c):
            hop = hb.hopp(bas[j])
            if i == j:
                mat[i][j] = bi.nu(i,bas[i])*a
            else:
                if hop is not None:
                    mat[i][j] = hb.dp(bas[i], hop)*b             
    return mat

