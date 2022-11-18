from primes import primes, isPrime


def test(n):
  for p in primes():
    if p > n:
      return True
    for s in range(1, 1000):
      n1 = p + 2*s**2
      if n == n1:
        return False
      if n1 > n:
        break
  


for i in range(1, 100000, 2):
  if test(i) and not isPrime(i):
    print("This is what we want:", i)