import itertools

class Memoize:
    def __init__(self, func): 
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache: 
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

MOD = 10**6

@Memoize
def P(n):
  if (n == 0):
    return 1
  if (n < 0):
    return 0
  summ = 0
  for k in range(1, n+1):
    n1 = n-k*(3*k-1)//2
    n2 = n-k*(3*k+1)//2
    summ = ( summ + (-1)**(k+1)*(  P(n1) + P(n2)  ))%MOD
    if n1 <= 0:
      break
      
  return summ


for n in itertools.count(1):
  if n%1000 == 0:
    print(n)
  if P(n)%MOD == 0:
    print(n)
    exit()