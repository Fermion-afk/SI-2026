import Interface.session as ss
import Basis_operations.binary as bi
import numpy as np

def run(va, ve):
    def pause():
        input("Press Enter to continue")
    cutoff = int(input(f"enter number of excited states to include (max {len(va)-1}): "))

    def degen(va, tol=1e-8):
        for i in range(1, len(va)):
            if abs(va[i] - va[0]) > tol:
                return i
        return len(va)
    # diagonalize mu_x within degenerate subspace (field-independent)
    def degen_sub_dia(va, ve):
        k = degen(va)
        if k != 1:
            ve_dash = ve[:, :k]
            mat = np.zeros((k, k))
            for i in range(k):
                for j in range(k):
                    mat[i,j] = float(ve_dash[:,i] @ (mu_fock[0] * ve_dash[:,j]))
            _, vec = np.linalg.eigh(mat)
            ve_corr = ve_dash @ vec
            return va[:k], ve_corr, k
        else:
            return va[:1], ve[:,:1], 1
        
    ba = ss.ses["bas"]["bas"]
    m = ss.ses["sys"]["n"]//2
    cords = ss.ses["sys"]["coords"]
    c = ss.ses["sys"]["c"]
    mu_fock = np.zeros((2,c))
    for idx, l in enumerate(ba):
        for k in range(m):
            mu_fock[0, idx] += cords[k][0]*(bi.nus(2*k,l)-1)  
            mu_fock[1, idx] += cords[k][1]*(bi.nus(2*k,l)-1)  

    va_d, ve_d, k = degen_sub_dia(va, ve)
    va_nd = va[k:k+cutoff]
    ve_nd = ve[:, k:k+cutoff]
    N_nd = ve_nd.shape[1]

    # --- precompute all transition dipole matrices via matrix multiplication ---
    # since mu is diagonal in Fock basis:
    # <psi_m|mu_a|psi_n> = sum_alpha C_alpha^(m)* mu_fock[a,alpha] C_alpha^(n)
    #                     = ve[:,m] . (mu_fock[a] * ve[:,n])

    # M_gd[a,n] = <psi_n|mu_a|psi_0> — ground to excited, shape (2, N_nd)
    M_gd = np.zeros((2, N_nd))
    for a in range(2):
        g0 = mu_fock[a] * ve_d[:,0]    # elementwise: mu_a * ground state coeffs
        M_gd[a] = ve_nd.T @ g0         # project onto all excited states

    # M_nd[a,m,n] = <psi_m|mu_a|psi_n> — excited to excited, shape (2, N_nd, N_nd)
    M_nd = np.zeros((2, N_nd, N_nd))
    for a in range(2):
        # ve_nd.T @ diag(mu_fock[a]) @ ve_nd
        M_nd[a] = ve_nd.T @ (mu_fock[a,:,None] * ve_nd)

    # M_dd[a] = <psi_0|mu_a|psi_0> — ground state diagonal, shape (2,)
    M_dd = np.zeros(2)
    for a in range(2):
        M_dd[a] = ve_d[:,0] @ (mu_fock[a] * ve_d[:,0])

    def sus(M_gd, M_nd, M_dd, va_d, va_nd):

        # energy denominators — shape (N_nd,)
        dE = va_nd - va_d[0]

        def alpha(a, b):
            # alpha_ab = sum_n <0|mu_a|n><n|mu_b|0> / (E_n - E_0)
            return np.sum(M_gd[a] * M_gd[b] / dE)

        def beta(a, b, c):
            # term 1: sum_mn <0|mu_a|m><m|mu_b|n><n|mu_c|0> / (dE_m * dE_n)
            w   = np.outer(1/dE, 1/dE)
            t1  = np.einsum('m,mn,n,mn->', M_gd[a], M_nd[b], M_gd[c], w)
            # term 2: <0|mu_a|0> * sum_n <0|mu_b|n><n|mu_c|0> / dE_n^2
            t2  = M_dd[a] * np.sum(M_gd[b] * M_gd[c] / dE**2)
            return t1 - t2

        def gamma(a, b, c, d):
            # term 1: sum_lmn <0|mu_a|l><l|mu_b|m><m|mu_c|n><n|mu_d|0>
            #         / (dE_l * dE_m * dE_n)
            w3  = np.einsum('l,m,n->lmn', 1/dE, 1/dE, 1/dE)
            t1  = np.einsum('l,lm,mn,n,lmn->', M_gd[a], M_nd[b], M_nd[c], M_gd[d], w3)
            # term 2: sum_mn <0|mu_a|m><0|mu_b|0><0|mu_c|n><n|mu_d|0>... wait
            # term 2: <0|mu_b|0> * sum_mn <0|mu_a|m><0|mu_c|n><n|mu_d|0>
            #         / (dE_m^2 * dE_n)
            w2  = np.outer(1/dE**2, 1/dE)
            t2  = M_dd[b] * np.einsum('m,n,n,mn->', M_gd[a], M_gd[c], M_gd[d], w2)
            return t1 - t2

        def susceptibility():
            print("\nALPHA (x2 prefactor)")
            print(f"alphaxx = {2*alpha(0,0):.6f}")
            print(f"alphaxy = {2*alpha(0,1):.6f}")
            print(f"alphayy = {2*alpha(1,1):.6f}")
            print("\nBETA (x6 prefactor)")
            print(f"betaxxx = {6*beta(0,0,0):.6f}")
            print(f"betaxxy = {6*beta(0,0,1):.6f}")
            print(f"betaxyy = {6*beta(0,1,1):.6f}")
            print(f"betayyy = {6*beta(1,1,1):.6f}")
            print("\nGAMMA (x24 prefactor)")
            print(f"gammaxxxx = {24*gamma(0,0,0,0):.6f}")
            print(f"gammaxxxy = {24*gamma(0,0,0,1):.6f}")
            print(f"gammaxxyy = {24*gamma(0,0,1,1):.6f}")
            print(f"gammaxyyy = {24*gamma(0,1,1,1):.6f}")
            print(f"gammayyyy = {24*gamma(1,1,1,1):.6f}")
            pause()

        susceptibility()

    sus(M_gd, M_nd, M_dd, va_d, va_nd)