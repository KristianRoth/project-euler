from primes import primes
N = 5*10**7 #5*10**7

isGood = [False]*(N)





for p1 in primes():
  P1 = p1**4
  if P1 > N:
    break
  for p2 in primes():
    P2 = p2**3
    if P1 + P2 > N:
      break
    for p3 in primes():
      summ = P1 + P2 + p3**2
      if summ < N:
        isGood[summ] = True
      if summ > N:
        break



print(sum([1 if isGood[i] else 0 for i in range(0, N)]))