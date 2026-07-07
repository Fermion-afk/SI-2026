def merge(l1,l2):
  x1 = len(l1)
  x2 = len(l2)
  x = x1 + x2
  l = [0]*(x)
  for i in range(x):
    if i%2 == 0:
      try:
        if l1[i//2] == 1:
          l[i] = 1
      except IndexError:
        if l2[i//2] == 1:
          l[i] = 1
    else:
      try:
        if l2[i//2] == 1:
          l[i] = 1
      except IndexError:
        if l1[i//2] == 1:
          l[i] = 1
  return(l)

def plus(l1,l2):
  c = []
  def ino(l):
    if not isinstance(l, list):
        return False

    for x in l:
        if isinstance(x, list):
            for y in x:
                if isinstance(y, list):
                    return False
            return True

    return False
  if(ino(l1) and ino(l2)):
    for i in l1:
      for j in l2:
        c.append(merge(i,j))
    return(c)
  elif(ino(l1) or ino(l2)):
    if(ino(l1)):
      for i in l1:
        c.append(merge(i,l2))
      return(c)
    else:
      for i in l2:
        c.append(merge(l1,i))
      return(c)
  else:
    c.append(merge(l1,l2))
    return(c)
#this function creates the ground state of given n and k in binary hashing
def gr(x,y):
    l = b(0)
    for i in range(y):
        l = tg(l,x-i)
    return l

con.va = np.array([
    -4.03059681e+00, -1.16994586e-31, 0.00000000e+00, 
     0.00000000e+00,  1.68567823e+00, 5.71627505e+00
])
con.ve = np.array([
        [-4.54712667e-01, -1.86286140e-16,  0.00000000e+00,  0.00000000e+00, -7.07106781e-01, -5.41513057e-01],
        [ 0.00000000e+00, -1.00000000e+00,  0.00000000e+00, -1.01465364e-17,  2.88733439e-16,  0.00000000e+00],
        [ 5.41513057e-01,  1.11022302e-16,  0.00000000e+00,  7.07106781e-01, -7.67529396e-17, -4.54712667e-01],
        [-5.41513057e-01,  1.11022302e-16,  0.00000000e+00,  7.07106781e-01,  4.09944750e-17,  4.54712667e-01],
        [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
        [-4.54712667e-01,  2.22044605e-16,  0.00000000e+00,  0.00000000e+00,  7.07106781e-01, -5.41513057e-01]
    ])

