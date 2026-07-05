import config as con
import Basis_operations.operators as op
va = []
ve = [[],[]]
c_o = con.c

def a(i,x,y):
    k = 0 
    for j in range(i+1,c_o):
        k += op.expval2(ve[j],op.dm_x,ve[i])*op.expval2(ve[j],op.dm_x,ve[i])/(va[j] - va[i])
    return 2*k

def b(i,x,y,z):
    k = 0
    

