
def hasSameDigits(a, b):
  b = str(b)
  for da in str(a):
    if da not in b:
      return False
    b = b.replace(da, "")
  return True

def test(n):
  for x in range(1, 7):
    if not hasSameDigits(n, n*x):
      return False
  return True

for i in range(1, 10000000):
  if test(i):
    print(i)