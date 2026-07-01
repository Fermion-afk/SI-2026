import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh

def numdense(mat):
    evals,evecs = np.linalg.eigh(mat)
    return evals,evecs

def scidense(mat):
    evals,evecs = eigh(mat)
    return evals,evecs

def scispa(mat):
    evals,evecs = eigsh(mat,k=5,which = "SA")
    return evals,evecs[:][:4]

