from itertools import permutations


def cubes():
  for i in range(1, 100000):
    yield i**3


def getDigits(n):
  return [int(x) for x in str(n)]

def getNumber(digits):
  return int("".join([str(x) for x in digits]))

def getKey(n):
  digits = getDigits(n)
  digits.sort(reverse=True)
  return getNumber(digits)

permGroups = dict()
c = 1
for cube in cubes():
  c += 1
  if c%10000 == 0:
    print(permGroups)
  key = getKey(cube)
  if key == 987655433210:
    print("halloo", cube)
  if key in permGroups:
    permGroups[key] += 1
    if permGroups[key] == 5:
      print("this is what we want:", key, permGroups[key])
      exit()
  else:
    permGroups[key] = 1


