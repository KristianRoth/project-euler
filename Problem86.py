import math, itertools

class Memoize:
    def __init__(self, func): 
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache: 
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

@Memoize
def countM(M):
  if(M == 0):
    return 0
  count = countM(M-1)
  a = M 
  for b in range(1, a+1):
    for c in range(1, b+1):
      if math.sqrt(a**2+(b+c)**2).is_integer():
        count += 1
  return count


for M in itertools.count(1):
  c = countM(M)
  if M%100 == 0:
    print(M, c)
  if c >= 10**6:
    print(M, c)
    exit()


