import numpy as np
import config as con
import hubbard as hb
import Basis_operations.binary as bi
import Basis_operations.operators as op

def main_huckel():
    bas = con.ba
    dim = con.c
    mat = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            hop = hb.hopp(bas[j])
            if i == j:
                if con.run2:
                    mat[i][j] = bi.nu(i,bas[i]) + op.fi_re(con.x_f,con.y_f,bas[j])
                else:
                    mat[i][j] = bi.nu(i,bas[i])
            else:
                if hop is not None:
                    mat[i][j] = hb.dp(bas[i], hop)*con.b             
    return mat

