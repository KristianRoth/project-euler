import itertools, math

def test(l, x):
  for t in l:
    if (t[1] == x[0] and t[0] == x[1]) or (t[0] == x[0] and t[1] == x[1]):
      return True
  return False

def generate(pmax):
  for m in itertools.count(1):
    m2 = m**2
    if 2*m*(m+1) > pmax:
      return
    for n in range(1, m):
      n2 = n**2
      for k in itertools.count(1):
        pyth = (k*(m2 - n2), k*(2*m*n), k*(m2 + n2))
        if sum(pyth) > 1500001:
          break
        yield pyth

triag = dict()


for x in generate(5000000):
  summ = sum(x)
  if summ in triag:
    if not test(triag[summ], x):
      triag[summ] += [x]
  else:
    triag[summ] = [x]

count = 0
for i, l  in triag.items():
  if len(l) == 1:
    count +=1

print(count)
