from math import comb
from functools import cache

@cache #memoization
# this just the choose function with x choose y()
def ch(x,y):
    if x < y:
        return 0
    else:
        return comb(x,y) 
# given a index this function gives out the corresponding combination 
def com(n,x,y):
    l = []
#vlarge here find out the maximum possible value of v < n such that ch(v,x) < y
    def vlarge(n,x,y):
        if y == 0: 
            return x-1 
        z = 0
        for i in range(n):
            if ch(n-(i+1),x) < y:
                z = n - (i+1)
                break 
        return z
    k = n
    for i in range(y):
        m = vlarge(x,y-i,k)
        l.append(m)
        k = k - ch(m,y-i)
    return l

# this function creates all the possible combinations of given n and k 
def per(x,y):
    z = int(ch(x,y))
    l = []
    for i in range(z):
        l.append(com(i+1,x,y))
    return l

#this the creation and annihilation operator together
#the first argument is the index of creation operator and the second argument is index of the annihilation operator ,
#the third one is the combination in combinadic representation
def a(x,l): #this is the annihilation operator
        k = set(l)
        if x not in k: #checks whether orbital with x index is occupied or not
            return 0, None
        g = 0
        for i in range(1,len(l)+1):
            if l[-i] == x:
                del l[-i]
                break
            g += 1
        return g,l

def c(y,l): #this is the creation operator
        k = set(l)
        if y in k:  #checks whether orbital with y index is occupied or not
            return 0, None
        
        h = 0
        for i in range(1,len(l)+1):
            if i == len(l):
                l.insert(-i,y)
            elif l[-i-1] > y:
                l.insert(-i,y)
                break
            h += 1
        return h,l

def ca(y,x,l):
    
    g,l1 = a(x,l)
    h,l2 = c(y,l1)

    return (g+h)%2,l2

