import config as con
import Basis_operations.basis as ba
import Basis_operations.binary as bi

def dp(v1,v2): #it is expected that v1 is a hash of a vector and v2 is [n,# of vector] where n is a integer
    if v1 == v2[1]:
        return v2[0]
    else:    
        return 0

def exp(fun,evec): #this function give the expectation value of operator(fun()) on # of vector evec
    k = 0
    for i in evec:
        for j in evec:
            k += dp(i,fun(j))
    return k

def double_occ(evec,i):
    k = bi.nus(i,evec)
    return[k,evec]

def opt():
    def __init__(self,h):
        self.opt = h
    def op(self,l):
        return op(l)

def post_opt():
    def __init__(self,h,l):
        self.opt = h
        self.vec = l

