from primes import isPrime, primes

def getDigits(n):
  return [int(x) for x in str(n)]

def isPerm(a, b):

  da = getDigits(a)
  db = getDigits(b)
  da.sort()
  db.sort()
  for i in range(0, 4):
    if da[i] != db[i]:
      return False
  return True
  

for first in primes(1000, 10000):
  for offset in range(2, (10000-first)//2+1):
    if isPrime(first + offset) and isPrime(first + 2*offset) and isPerm(first, first + offset) and isPerm(first, first + 2*offset):
      print(first, first + offset, first + 2*offset)




