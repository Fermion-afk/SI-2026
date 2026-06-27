from functools import cache
#this function create the ground (reference) state
def gr(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  return l
#this creates the single excitation (by considering the gr() state as reference)
def cis(x,y):
  l = gr(x,y)
  c1 = []
  z = x - y
  for i in range(z):
    l1 = l[:]
    l1[y-1] = 0;l1[y+i] = 1
    c1.append(l1)
  return c1
#this create doubles excitations
def cisd(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  c2 = []
  c1 = cis(x,y)
  z = y - 1
  for i in c1:
    k = z
    while(i[k] == 0):
      l2 = i[:]
      l2[z-1] = 0;l2[k] = 1
      c2.append(l2)
      k += 1
  return c2
#this create triple excitations
def cisdt(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  c3 = []
  c2 = cisd(x,y)
  z = y - 1
  for i in c2:
    k = z - 1
    while(i[k]==0):
      l3 = i[:]
      l3[z-2] = 0;l3[k] = 1
      c3.append(l3)
      k += 1
  return c3
#full CI 
@cache #memoization
def per(x,y):
  #Base cases
  if y < 0 or y > x:
    return []

  if x == 0:
    return [[]]

  if x == 1:
    if y == 0:
      return [[0]]
    elif y == 1:
      return [[1]]
    else:
      return []

  if y == 0:
    return [[0]*x]

  if x == y:
    return [[1]*x]

  c = []
  #Recursion term
  for i in range(y+1):

    a = per(x//2, y-i)
    b = per(x - x//2, i)

    for p in a:
      for q in b:
        c.append(p+q)

  return c

"""this function takes the basis set and creates a hash with entries being the corresponding integer
(combination are considered binary string)"""
def binary_hash(l):
    k = []
    for i in l:
      j = "".join(str(k) for k in i)
      k.append(int(j,2))
      k.sort(reverse=True)
    return k


