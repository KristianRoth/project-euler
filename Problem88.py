from primes import divisors, isPrime
from itertools import count


def prod(n):
  pr = 1
  for i in n:
    pr *= i
  return pr


def p(n):
  if n == 1: return []
  if isPrime(n): return [n]
  yield [n]
  for x in divisors(n):
    if x == n or x == 1:
      continue
    yield [n//x] + [x]
    for ys in p(x):
      yield [n//x] + ys

def find(n, k):
  for x in p(n):
    if n == sum(x) + k - len(x):
      return True
  return False

finals = set()
for k in range(2, 12001):
  if k%100 == 0:
    print(k, sum(finals))
  for n in count(k):
    if find(n, k):
      finals.add(n)
      break

print(sorted(list(finals)))
print(sum(finals))

