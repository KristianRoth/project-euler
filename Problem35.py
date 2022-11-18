from itertools import permutations

def getDigits(n):
  return [int(x) for x in str(n)]

def getNumber(d):
  return int(''.join(map(str, d)))

def isPrime(n):
  if n == 1:
    return False
  for i in range(2, n**1/2+1):
    if n%i == 0:
      return False
  return True

def getNext(n):
  digits = getDigits(n)
  first = digits.pop()
  digits.insert(0, first)
  return getNumber(digits)

def isCircular(n):
  if any(d in [0, 2, 4, 8] for d in getDigits(n)):
    return False
  for i in range(0, len(str(n))):
    if not isPrime(n):
      return False
    n = getNext(n)
  return True

count = 0
for i in range(1, 1000000, 2):
  if i%100001 == 0:
    print("i: " + str(i))
  if isCircular(i):
    print(i)
    count += 1
    print("count: " + str(count))
print(count)


