import Interface.session as ss
""" for a integer n the bin(n) gives "0bxxxx" with the leading 0b represting it is in 
binary format ; b(n) chops of the leading term """
def b(n):
    return(bin(n)[2:])
"""this function toogles the nth bit of a number in its binary representation
;it returns a binary string including the leading terms"""
def tg(l,k):
    return l ^ (1 << k)

"""remember here n is the number of orbitals it must be declared 
somewhere before this block"""
def c(x,z): #creation operator
        n = ss.ses["sys"]["n"]
        if z == None:
             return 0,None
        e = ((z>>(n-1-x))&1) #checks if the xth orbital is already occupied or not
        if e == 1:
            return 0,None
        i_b = z >> (n-x)
        t = i_b.bit_count()
        return t%2,tg(z,n-1-x)

def a(y,z): # annihilation operator
        n = ss.ses["sys"]["n"]
        if z == None:
             return 0,None
        d = ((z>>(n-1-y))&1) #checks if the yth orbital is already empty or not
        if d == 0:
            return 0,None
        i_b = z >> (n-y)
        t = i_b.bit_count()
        return t%2,tg(z,n-1-y)      
                                                                                                                   
def ca(x,y,z): #creation and annihilation together 
    i,i1 = a(y,z) # i tracks phase change from action of annihilation operator 
    j,j1 = c(x,i1) # j tracks phase change from action of creation operator
    return (i+j)%2,j1

def nu(x,l): #number operator for spin orbital
    n = ss.ses["sys"]["n"]
    e = ((l>>(n-1-x))&1)
    return e

def nus(x,l): #number operator for spatial orbital
    n = ss.ses["sys"]["n"]
    e = ((l>>(n-1-x))&1)
    r = ((l>>(n-2-x))&1)
    return e+r