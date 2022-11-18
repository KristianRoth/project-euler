

matrix = []
with open("p081_matrix.txt") as file:
  for a in file:
    
    matrix.append([int(x) for x in a.split(",")])

def getM(a, b):
  if a < 0:
    return 1107055572494826611310457449608783553916328095645103
  if a > len(matrix) - 1:
    return 1107055572494826611310457449608783553916328095645103
  if b < 0:
    return 1107055572494826611310457449608783553916328095645103
  if b > len(matrix) - 1:
    return 1107055572494826611310457449608783553916328095645103
  return matrix[getR(a)][getR(b)]

def getR(a):
  if a < 0:
    return 0
  if a > len(matrix) - 1:
    return len(matrix) - 1
  return a

for a in range(79, -1, -1):
  for b in range(79, -1, -1):
    if (a == b == 79): continue
    matrix[a][b] += min(getM(a+1, b), getM(a, b+1))

print(matrix[0][0])

