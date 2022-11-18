from primes import isPrime

def fun(a, b, n):
  return n**2 + a*n + b


max = 0
for a in range(-1000, 1001):
  if a%100 == 0:
    print("A: " + str(a))
  for b in range(-1000, 1001):
    i = 0
    for i in range(0, 100000):
      if (not isPrime(fun(a, b, i))):
        if (max < i):
          max = i
          print("a: " + str(a) + " b: " + str(b) + " times: " + str(max))
        break


