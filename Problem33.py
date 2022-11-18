def getDigits(n):
  return [int(x) for x in str(n)]

def getNumber(d):
  return int(''.join(map(str, d)))

def getCommon(a, b):
  da = getDigits(a)
  db = getDigits(b)
  for i in range(1, 10):
    if i in da and i in db:
      return i
  return False

def remove(a, n):
  digits = getDigits(n)
  digits.remove(a)
  return getNumber(digits)


def good(b, a):
  x = getCommon(a, b)
  if not x:
    return False
  ax = remove(x, a)
  bx = remove(x, b)
  if (ax == 0 or bx == 0):
    return False
  if (1.0*b)/(1.0*a) == (1.0*bx)/(1.0*ax):
    print(str(b) + "/" + str(a) + " = " + str(bx) + "/" + str(ax))
    return True
  return False



for a in range(10, 100):
  for b in range(10, a):
    good(b, a)