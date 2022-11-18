from primes import totient

def getDigits(n):
  return [int(x) for x in str(n)]

def isPerm(a, b):

  da = getDigits(a)
  db = getDigits(b)
  if len(da) != len(db):
    return False
  da.sort()
  db.sort()
  for i in range(0, len(da)):
    if da[i] != db[i]:
      return False
  return True


minn = 1000
nminn = 0
for i in range(2, 10**7):
  if (i%100000 == 0):
    print(i)
  t = totient(i)
  if (isPerm(t, i)) and (i*1.0)/t < minn:
    minn = (i*1.0)/t
    nminn = i

print(nminn, minn)
