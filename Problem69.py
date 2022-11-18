from primes import primes



summ = 1
for p in primes():
  if (summ * p > 10**6):
    print(summ)
    exit()
  summ *= p