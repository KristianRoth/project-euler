import math, itertools, sys
sys.setrecursionlimit(100000)

def first(d):
  x = math.floor(math.sqrt(d))
  return (x, 1, x**2-d, d)

def gen(N):
  x = math.floor(math.sqrt(N))
  for i in itertools.count(0):
    yield x + i
    if x - i > 0:
      yield x - i

def iteration(x):
  (a, b, k, N) = x
  if k == 1:
    return (a, b)
  for m in gen(N):
    if (a+b*m)%k == 0:
      break
  return iteration( ( (a*m+N*b)//abs(k), (a+b*m)//abs(k), (m**2-N)//k, N ) )

maxx = 0
xd = 0
for d in range(13, 1001):
  if not math.sqrt(d).is_integer():
    (x, y) = iteration(first(d))
    if x > maxx:
      maxx = x
      xd = d
      print("d =", xd, "x =", maxx)

print(maxx, xd)