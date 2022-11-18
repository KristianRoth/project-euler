import math

N = 100000
pent = N*[None]

def fun(n):
  if pent[n] is None:
    pent[n] = int((n*(3*n-1))/2)
  return pent[n]

def isPent(n):
  x = (1 + math.sqrt(24*n + 1))/6.0
  if x == int(x):
    return True


def funGenerator(n = N**2):
  for i in range(1, N**2):
    p = fun(i)
    if p > n:
      return
    yield p


count = 1
for a in funGenerator():
  for b in funGenerator(a):
    count += 1
    if count%100000 == 0:
      print(a, b, a+b, a-b)

    if isPent(a + b) and isPent(a - b):
      print("This is what we want:", (a-b) )