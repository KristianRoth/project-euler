import math

def ncr(n, r):
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

count = 0
for n in range(23, 101):
  for r in range(0, n):
    if (ncr(n, r) > 10**6):
      count += 1
print(count)