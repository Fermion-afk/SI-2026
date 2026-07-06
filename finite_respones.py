import config as con
import Basis_operations.operators as op
import main_1 
import numpy as np
from functools import cache

x = float(input("enter the x field component"))
y = float(input("enter the y field component"))

global va_d,ve_d
global va_nd,ve_nd

class per:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def di(self,l1,l2):
        k = self.x*op.expval2(l1,op.dm_x,l2) 
        k += self.y*op.expval2(l1,op.dm_y,l2)
        return k

perb = per(x,y)
     
def degen(va):
    k = va[0]
    for i in range(1,len(va)):
        if va[i] != k:
            return i
    else:
        return len(va)
    
dm_cache = {}
def t_dm(l1, l2, x):
    key = (tuple(l1), tuple(l2), x)
    if key not in dm_cache:
        if x == 0: dm_cache[key] = op.expval2(l1, op.dm_x, l2)
        elif x == 1: dm_cache[key] = op.expval2(l1, op.dm_y, l2)
    return dm_cache[key]
        
def degen_sub_dia(va,ve):
    k = degen(va)
    ve_dash = ve[:,:k]
    mat = np.zeros((k,k))
    for i in range(k):
        for j in range(k):
            mat[i,j] = perb.di(ve_dash[:,i],ve_dash[:,j])
    val,vec = main_1.dia(mat)
    ve_corr = ve_dash @ vec 
    E_corr = np.array([va[0] + val[i] for i in range(k)])
    return E_corr, ve_corr ,k
    
va_d, ve_d, k = degen_sub_dia(con.va, con.ve)
va_nd = con.va[k:]
ve_nd = con.ve[:, k:]

N_nd = ve_nd.shape[1]
N_d  = ve_d.shape[1]

# precompute transition dipole matrices — shape (2, N_nd, N_d)
M_gd = np.zeros((2, N_nd, N_d))
for a in range(2):
    for n in range(N_nd):
        for i in range(N_d):
            M_gd[a,n,i] = t_dm(tuple(ve_nd[:,n]), tuple(ve_d[:,i]), a)

# precompute excited-excited transition dipole — shape (2, N_nd, N_nd)
M_nd = np.zeros((2, N_nd, N_nd))
for a in range(2):
    for m in range(N_nd):
        for n in range(N_nd):
            M_nd[a,m,n] = t_dm(tuple(ve_nd[:,m]), tuple(ve_nd[:,n]), a)

# precompute ground-ground diagonal — shape (2, N_d)
M_dd = np.zeros((2, N_d))
for a in range(2):
    for i in range(N_d):
        M_dd[a,i] = t_dm(tuple(ve_d[:,i]), tuple(ve_d[:,i]), a)

def alpha(a, b, i):
    k = 0
    for n in range(N_nd):
        k += M_gd[a,n,i] * M_gd[b,n,i] / (va_nd[n] - va_d[i])
    return k

def beta(a, b, c, i):
    k = 0
    for m in range(N_nd):
        for n in range(N_nd):
            dm_E = (va_nd[m]-va_d[i]) * (va_nd[n]-va_d[i])
            k += M_gd[a,m,i] * M_nd[b,m,n] * M_gd[c,n,i] / dm_E
    mu_00 = M_dd[a,i]
    for n in range(N_nd):
        dE_n = (va_nd[n]-va_d[i])**2
        k -= mu_00 * M_gd[b,n,i] * M_gd[c,n,i] / dE_n
    return k

def gamma(a, b, c, d, i):
    k = 0
    for l in range(N_nd):
        for m in range(N_nd):
            for n in range(N_nd):
                dl = va_nd[l]-va_d[i]
                dm = va_nd[m]-va_d[i]
                dn = va_nd[n]-va_d[i]
                k += (M_gd[a,l,i] * M_nd[b,l,m] *
                      M_nd[c,m,n] * M_gd[d,n,i]) / (dl*dm*dn)
    for m in range(N_nd):
        for n in range(N_nd):
            dm2 = (va_nd[m]-va_d[i])**2
            dn  =  va_nd[n]-va_d[i]
            k -= (M_gd[a,m,i] * M_dd[b,i] *
                  M_gd[c,n,i] * M_gd[d,n,i]) / (dm2*dn)
    return k