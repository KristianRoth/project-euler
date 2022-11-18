import math

def getIntegerRight(p):
  count = 0
  for a in range(1, p):
    for b in range(a+1, p):
      c = math.sqrt(a**2 + b**2)
      if (a+b+c == p):
        count += 1
  return count






maxx = 0
for i in range(1, 1001):
  count = getIntegerRight(i)
  if count > maxx:
    maxx = count
    print(i)
    print(count)