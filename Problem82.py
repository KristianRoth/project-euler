matrix = []
def prnt(A):
  print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))

with open("p081_matrix.txt") as file:
  for a in file:
    
    matrix.append([int(x) for x in a.split(",")])

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

inf = float("inf")
lenn = len(matrix)
dist = []
for i in range(lenn):
  dist.append([inf]*lenn)

vert = [(-1, -1)]
distEnd = [inf]



for a in range(0, lenn):
  for b in range(0, lenn):
    vert.append((a, b))
vert.append((100,100))

def distance(x):
  (a, b) = x
  if a == -1:
    return 0
  if a == 100:
    return distEnd[0]
  return dist[a][b]

def setDist(x, d):
  (a, b) = x
  if a == -1:
    return
  if a == 100:
    distEnd[0] = d
    return
  dist[a][b] = d



def length(x):
  (a, b) = x
  if a == -1:
    return 0
  if a == 100:
    return 0
  return matrix[a][b]

def getMin():
  minn = inf
  ver = None
  for v in vert:
    d = distance(v)
    if d < minn:
      minn = d
      ver = v
  
  return (ver, minn)

def next(x):
  (a, b) = x
  if a == -1:
    for i in range(0, lenn):
      yield (i, 0)
    return
  if a == 100:
    return 
  if a < lenn-1:
    yield (a+1, b)
  if a >= 1:
    yield (a-1, b)
  if b < lenn-1:
    yield (a, b+1)
  else:
    yield (100, 100)

def Dijkstra():
  while len(vert) != 0:
    (u, distu) = getMin()
    vert.remove(u)
    for neigh in next(u):
      alt = distu + length(neigh)
      if alt < distance(neigh):
        setDist(neigh, alt)
    
  return distance((100, 100))

print(Dijkstra())


# prnt(matrix)
# print()
# prnt(dist)
