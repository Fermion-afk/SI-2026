import Interface.session as ss
import Basis_operations.binary as bi
import numpy as np


def _state_data():
    ba = ss.ses["bas"]["bas"]
    m = ss.ses["sys"]["n"] // 2
    cords = ss.ses["sys"]["coords"]
    return ba, m, cords


def expval(f, l): # calculates expectation value <l|f|l>
    k = 0
    ba, m, _ = _state_data()
    for i in range(m):
        k += (abs(l[i])**2)*(f(ba[i]))
    return k

def expval2(l1, f, l2): # calculates transition matrix element <l1|f|l2>
    k = 0
    ba, m, _ = _state_data()
    for i in range(m):
        k += np.conj(l1[i])*l2[i]*(f(ba[i]))
    return k

def double_occ(evec): #give the expectation value of double occupany in a state
    k = 0
    _, m, _ = _state_data()
    for i in range(m):
        if bi.nus(2*i,evec) == 2:
            k += 1
    return k

def dm_x(l):#x component of the dipole moment
    k = 0
    _, m, cords = _state_data()
    for i in range(m):
        k += cords[i][0]*(bi.nus(2*i,l)-1)
    return k

def dm_y(l):#y component of the dipole moment
    k = 0
    _, m, cords = _state_data()
    for i in range(m):
        k += cords[i][1]*(bi.nus(2*i,l)-1)
    return k

def fi_re(x,y,l):
    k = 0 
    k += x*dm_x(l)
    k += y*dm_y(l)
    return k

def e_d(l):
    ba, m, _ = _state_data()
    den = np.zeros(m)
    for idx, coeff in enumerate(l):
        if abs(coeff) < 1e-12:
            continue
        k = ba[idx]  
        for i in range(m):
            n_site = bi.nus(2*i, k)
            den[i] += (abs(coeff)**2)*n_site
    return den

def dd_corr(l):
    ba, m, _ = _state_data()
    n_exp  = np.zeros(m) 
    nn_exp = np.zeros((m, m))
    for idx, coeff in enumerate(l):
        if abs(coeff) < 1e-12:
            continue
        l = ba[idx]
        prob = abs(coeff)**2
        n_site = np.array([bi.nus(2*site, l) for site in range(m)])
        n_exp += prob*n_site
        nn_exp += prob*np.outer(n_site, n_site)
    C = nn_exp - np.outer(n_exp, n_exp)
    return C