
from primes import primes


l = [1] + [0] * 100
for coin in primes(0, 100):
	for i in range(coin, 100+1):
		l[i] += l[i - coin]

print(l)
print(l[100])

for i, x in enumerate(l):
  if x > 5000:
    print(i)
    break

