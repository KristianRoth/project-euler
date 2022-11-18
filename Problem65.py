import sys
sys.setrecursionlimit(10000)
from fractions import Fraction

eulers = []

for i in range(1, 334):
  eulers.append(1)
  eulers.append(i*2)
  eulers.append(1)

eulers.append(1)







def euler(n = 0):
  if n == 100-1:
    return 0
  return Fraction(1, eulers[n] + euler(n+1))
  

print(sum([int(x) for x in str((euler()+2).numerator)]))