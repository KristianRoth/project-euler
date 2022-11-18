from primes import primes
from itertools import combinations

NUMBER_OF_DIGITS = 3

def getDigits(n):
  return [x for x in str(n)]

def getKey(digits, i, c):
  for perm in combinations(range(c), NUMBER_OF_DIGITS):
    num = ""
    count = 0
    for x in digits:
      if x==i:
        if count in perm:
          num += "*"
        else:
          num += x
        count += 1
      else:
        num += x
    yield num



def get(n):
  digits = getDigits(n)
  for i in range(0, 10):
    count = digits.count(str(i))
    if count >= NUMBER_OF_DIGITS:
      for x in getKey(digits, str(i), count):
        yield x


counts = dict()
for p in primes():
  for key in get(p):
    if key:
      if key in counts:
        count = counts[key]
        if count == 7:
          print(key, p)
        counts[key] += 1
      else:
        counts[key] = 1





# 100109

# "524**": 1
# "52***": 1
# "5*5**": 3

# x mod 3 == 0|1|2

# mod 0
# x + 0 + 0
# x + 3 + 3
# x + 6 + 6
# x + 9 + 9

# mod 2
# x + 1 + 1 
# x + 4 + 4
# x + 7 + 7

# mod 1
# x + 2 + 2 
# x + 5 + 5
# x + 8 + 8

