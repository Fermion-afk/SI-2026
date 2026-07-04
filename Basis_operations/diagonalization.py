from numpy import linalg
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh

def numdense(mat):
    evals,evecs = linalg.eigh(mat)
    return evals,evecs

def scidense(mat):
    evals,evecs = eigh(mat)
    return evals,evecs

def scispa(mat):
    evals,evecs = eigsh(mat,k=7,which = "SA")
    return evals,evecs[:,:6]

