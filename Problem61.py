from itertools import permutations

def P3(n):
  return n*(n+1)//2

def P4(n):
  return n**2

def P5(n):
  return n*(3*n-1)//2

def P6(n):
  return n*(2*n-1)

def P7(n):
  return n*(5*n-3)//2

def P8(n):
  return n*(3*n-2)

def generator(P):
  n = 1
  while True:
    num = P(n)
    n += 1
    if (num < 1000):
      continue
    if (num > 9999):
      return
    yield num

def generatorS(P, prev):
  start = str(prev)[2:4]
  for n in generator(P):
    if str(n)[0:2] == start:
      yield n

def generatorSE(P, first, prev):
  end = str(first)[0:2]
  for n in generatorS(P, prev):
    if str(n)[2:4] == end:
      yield n



gens = [P3, P4, P5, P6, P7, P8]
for perm in permutations(gens):
  for p3 in generator(perm[0]):
    for p4 in generatorS(perm[1], p3):
      if p4 != p3:
        for p5 in generatorS(perm[2], p4):
          if p5 != p4 and p5 != p3:
            for p6 in generatorS(perm[3], p5):
              if p6 != p5 and p6 != p4 and p6 != p3:
                for p7 in generatorS(perm[4], p6):
                  if p7 != p6 and p7 != p5 and p7 != p4 and p7 != p3:
                    for p8 in generatorSE(perm[5], p3, p7):
                      if p8 != p7 and p8 != p6 and p8 != p5 and p8 != p4 and p8 != p3:
                        print([p3, p4, p5, p6, p7, p8])
                        print(sum([p3, p4, p5, p6, p7, p8]))