def isPrime(n):
  if n == 1:
    return False
  for i in range(2, n**1/2+1):
    if n%i == 0:
      return False
  return True

def getDigits(n):
  return [int(x) for x in str(n)]

def good(n):
  if any(d in [0, 2, 4, 8] for d in getDigits(n)):
    return False
  b = n
  while True:
    if not isPrime(n):
      return False
    if not len(str(n)) > 1:
      break
    n = int(str(n)[:-1])
  while True:
    if not isPrime(b):
      return False
    if not len(str(b)) > 1:
      break
    b = int(str(b)[1:])
  return True

summ = 0                
for i in range(100000, 1000000):
  if good(i):
    summ += i
    print("i:   " + str(i))
    print("Sum: " + str(summ))