def getDigits(n):
  return [int(x) for x in str(n)]

def uniq(n):
  dn = getDigits(n)
  return not 0 in dn and len(dn) == len(set(dn)) 

def unique(a, b):
  if (not uniq(a) or not uniq(b)):
    return False
  db = getDigits(b)
  for da in getDigits(a):
    if (da in db):
      return False
  return True

def contAll(a, b, c):
  digits = getDigits(a) + getDigits(b) + getDigits(c)
  for i in range(1, 10):
    if not i in digits:
      return False
  return True

def good(a, b):
  if not unique(a, b):
    return False
  c = a * b
  if unique(c, a) and unique(c, b) and contAll(a, b, c):
    print(str(a) + " x " + str(b) + " = " + str(c))
    return True
  else:
    return False

count = 0

products = []
for a in range(1, 50):
  for b in range(a+1, 4000):
    if good(a, b):
      count += 1
      products.append(a*b)
print(count)
print(sum(set(products)))
