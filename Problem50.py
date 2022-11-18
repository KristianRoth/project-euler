from primes import primes, isPrime


maxx = 0
summ = 0
for p in primes(1, 10**6):
  count = 1
  summ = p
  for p2 in primes(p+1, 10**6):
    count += 1
    summ += p2
    if (summ > 10**6):
      break
    if isPrime(summ) and count > maxx:
      maxx = count
      print("Alkuluku:", summ, "Summien määrä:", count, "Aloitus alkuluku:", p)


