import math



def fun(n, denom, fl):
  a = math.floor(denom/(math.sqrt(n)-fl))
  denom2 = (n-fl**2)//denom
  fl2 = -(fl-a*denom2)
  return (a, denom2, fl2)


def getSequence(n):
  a0 = math.floor(math.sqrt(n))
  denom = 1
  fl = a0
  lista = []
  for i in range(1, 1000):
    (a, denom, fl) = fun(n, denom, fl)
    lista.append(a)
  return lista

def isLoop(lista, loop):
  for inx, a in enumerate(lista):
      if loop[inx%len(loop)] != a:
        return False
  return True

def getLen(n):
  lista = getSequence(n)
  for i in range(1, 1000):
    loop = lista[:i]
    if isLoop(lista, loop):
      return len(loop)

sqrs = [i**2 for i in range(1, 101)]

count = 0
for n in range(1, 10000):
  if n%371 == 0:
    print(n) 
  if n not in sqrs:
    if getLen(n)%2 == 1:
      count += 1
print(count)