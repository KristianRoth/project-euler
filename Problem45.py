import math

def fun(n):
  return n*(2*n - 1)

def isPent(n):
  x = (1 + math.sqrt(24*n + 1))/6.0
  if x == int(x):
    return True

def isTria(n):
  x = (-1 + math.sqrt(8*n + 1))/2.0
  if x == int(x):
      return True


for i in range(1, 1000000):
  t = fun(i)
  if isPent(t) and isTria(t):
    print(t)