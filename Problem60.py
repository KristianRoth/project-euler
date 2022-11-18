from primes import primes, isPrime
from itertools import combinations, permutations


def isP(primes):
  return isPrime(int("".join([str(p) for p in primes])))

def isGood(primes):
  for comb in combinations(range(len(primes)), 2):
    for perm in permutations([primes[comb[0]], primes[comb[1]]]):
      if not isP(perm):
        return False
  return True


c = 0
candidates = []
for p in primes():
  c += 1
  if c%100 == 0:
    print("*************************************************************************")
    print("Count of Lenghts:", len([x for x in candidates if len(x) == 4]), len([x for x in candidates if len(x) == 3]), len([x for x in candidates if len(x) == 2]), len([x for x in candidates if len(x) == 1]))
    print("Current Prime:", p)
    print("Total candidates:", len(candidates))
  for cand in candidates:
    new = [p] + cand
    if isGood(new):
      if len(new) == 5:
        print(new)
        print(len(new))
      candidates.append(new)
  candidates.append([p])