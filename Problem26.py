

def rec(i, n):
  frac = []
  rem = []
  while True:
    if (i%n==0): 
      return 0
    if (i < n):
      i *= 10
      continue
    a = i/n
    r = i%n
    if (a in frac and rem[frac.index(a)] == r):
      return len("".join([str(int) for int in frac]))
    
    frac.append(a)
    rem.append(r)
    i = r
  
    

max = 0
for i in range(1, 1000):
  if i == 384 or i == 576 or i == 768: 
    continue
  cur = rec(1, i)
  if cur > max:
    max = cur
    print(i)

