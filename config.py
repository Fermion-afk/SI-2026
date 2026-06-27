from math import comb

n = 0 #number of spin orbitals
k = 0 #number of electrons
c = 0 #dimension of occupation number space
m = 0 #number of sites or atoms

a = 1 #onsite energy
b = 1 #hopping parameter
u = 1 #intrasite repulsion parameter

def ini1():
    global n,k,c,m

    n = int(input("input the number of spin orbitals"))
    k = int(input("enter the number of electrons"))

    c = comb(n,k)

    m = n//2

def ini2():
    global a,b,u
    
    a = float(input("Enter the value of onsite energy"))
    b = float(input("Enter the value of hopping parameter"))
    u = float(input("Enter the value of intrasite repulsion parameter"))

