from primes import isPrimeC
import time

def getNumber(d):
  return int(''.join(map(str, d)))

def isPandigital(n):
  s = str(n)
  if "0" in s: 
    return False
  digits = set([int(x) for x in s])
  for i in range(1, len(s) + 1):
    if i not in digits:
      return False
  return True

count = 1
for p in range(3, 10**8, 2):
  count += 1
  if isPandigital(p):
    if count%10**4== 0:
      print(p)
    if isPrimeC(p):
      print("This is prime that we are looking for " + str(p))

    


