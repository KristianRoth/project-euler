from itertools import permutations

def getNumber(d):
  return ''.join(map(str, d))

def generatePandigital():
  nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  perms = permutations(nums)
  for perm in perms:
    yield getNumber(perm)

def good(p):
  primes = [2, 3, 5, 7, 11, 13, 17]
  for i in range(1, 8):
    if int(p[i:i+3])%primes[i-1] != 0:
      return False
  return True

summ = 0
for p in generatePandigital():
  if good(p):
    print(p)
    summ += int(p)

print("Summa on: ", summ)