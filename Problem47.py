from primes import factors
import time

print("start")
start = time.time()
counter = 0
for i in range(1, 1000000):
  if len(set(factors(i))) == 4:
    counter += 1
  else:
    counter = 0
  if counter == 4:
    print("This is what we want:", i-3)
    print(i-3, factors(i-3))
    print(i-2, factors(i-2))
    print(i-1, factors(i-1))
    print(i, factors(i))
    print(time.time() - start)
    exit()
