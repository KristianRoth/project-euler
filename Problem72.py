from primes import totient

summ = -1
for i in range(1, 10**6+1):
  if i%1000 == 0:
    print(i, summ)
  summ += totient(i)
print(summ)