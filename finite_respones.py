import config as con
import Basis_operations.operators as op
import main_1 
import numpy as np
from functools import cache

def run(va,ve):
    global va_d,ve_d,va_nd,ve_nd
    global N_nd, N_d, M_gd, M_nd_mat, M_dd

    x = float(input("enter the x component of the field"))
    y = float(input("enter the y component of the field"))
    cutoff = int(input(f"enter number of excited states to include (max {len(va)-1}): "))

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
        if k != 1:
            ve_dash = ve[:,:k]
            mat = np.zeros((k,k))
            for i in range(k):
                for j in range(k):
                    mat[i,j] = perb.di(ve_dash[:,i],ve_dash[:,j])
            val,vec = np.linalg.eigh(mat)
            ve_corr = ve_dash@vec 
            E_corr = np.array([va[0] + val[i] for i in range(k)])
            return E_corr, ve_corr ,k
        else: 
            return va[:1], ve[:,:1], 1
        
    va_d, ve_d, k = degen_sub_dia(va, ve)
    va_nd = va[k:k+cutoff]     
    ve_nd = ve[:, k:k+cutoff]    

    N_nd = ve_nd.shape[1]
    N_d  = ve_d.shape[1]

    # precompute transition dipole — ground state only, shape (2, N_nd)
    M_gd = np.zeros((2, N_nd))
    for a in range(2):
        for n in range(N_nd):
            M_gd[a,n] = t_dm(tuple(ve_nd[:,n]), tuple(ve_d[:,0]), a)

    # precompute excited-excited transition dipole — shape (2, N_nd, N_nd)
    M_nd = np.zeros((2, N_nd, N_nd))
    for a in range(2):
        for m in range(N_nd):
            for n in range(N_nd):
                M_nd[a,m,n] = t_dm(tuple(ve_nd[:,m]), tuple(ve_nd[:,n]), a)

    # precompute ground-ground diagonal — scalar per component, shape (2,)
    M_dd = np.zeros(2)
    for a in range(2):
        M_dd[a] = t_dm(tuple(ve_d[:,0]), tuple(ve_d[:,0]), a)

    def sus(M_gd, M_nd, M_dd, va_d, va_nd):

        

        # precompute energy differences — shape (N_nd,)
        dE = va_nd - va_d[0]

        def alpha(a, b):
            return np.sum(M_gd[a] * M_gd[b] / dE)

        def beta(a, b, c):
            # term 1: M_gd[a,m] * M_nd[b,m,n] * M_gd[c,n] / (dE[m]*dE[n])
            # weight M_nd by outer product of 1/dE
            w = np.outer(1/dE, 1/dE)           # shape (N_nd, N_nd)
            t1 = np.einsum('m,mn,n,mn->', M_gd[a], M_nd[b], M_gd[c], w)
            # term 2: mu_00 * M_gd[b,n] * M_gd[c,n] / dE[n]^2
            t2 = M_dd[b] * np.sum(M_gd[b] * M_gd[c] / dE**2)
            return t1 - t2

        def gamma(a, b, c, d):
            w3 = np.einsum('l,m,n->lmn', 1/dE, 1/dE, 1/dE)  # shape (N_nd,N_nd,N_nd)
            # term 1: M_gd[a,l]*M_nd[b,l,m]*M_nd[c,m,n]*M_gd[d,n] / (dE[l]*dE[m]*dE[n])
            t1 = np.einsum('l,lm,mn,n,lmn->', M_gd[a], M_nd[b], M_nd[c], M_gd[d], w3)
            # term 2: M_gd[a,m]*M_dd[b]*M_gd[c,n]*M_gd[d,n] / (dE[m]^2 * dE[n])
            w2 = np.outer(1/dE**2, 1/dE)       # shape (N_nd, N_nd)
            t2 = M_dd[b] * np.einsum('m,n,n,mn->', M_gd[a], M_gd[c], M_gd[d], w2)
            return t1 - t2
        def susceptibilty():
            print("ALPHA")
            print(f"alphaxx = {2*alpha(0,0)}")
            print(f"alphaxy = {2*alpha(0,1)}")
            print(f"alphayy = {2*alpha(1,1)}")
            print("\nBETA")
            print(f"betaxxx = {6*beta(0,0,0)}")
            print(f"betaxxy = {6*beta(0,0,1)}")
            print(f"betaxyy = {6*beta(0,1,1)}")
            print(f"betayyy = {6*beta(1,1,1)}")
            print("\nGAMMA")
            print(f"gammaxxxx = {24*gamma(0,0,0,0)}")
            print(f"gammaxxxy = {24*gamma(0,0,0,1)}")
            print(f"gammaxxyy = {24*gamma(0,0,1,1)}")
            print(f"gammaxyyy = {24*gamma(0,1,1,1)}")
            print(f"gammayyyy = {24*gamma(1,1,1,1)}")
        
        susceptibilty()

    sus(M_gd,M_nd,M_dd,va_d,va_nd)
        

