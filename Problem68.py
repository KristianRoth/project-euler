from itertools import permutations

nums = [i for i in range(1, 11)]
def isValid(fgon):
  summ = sum(fgon[0])
  for i in range(5):
    if sum(fgon[i]) != summ:
      return False
  return True

def solSet(fgon):
  minn = 11
  minnx = 0
  for i in range(5):
    if fgon[i][0] < minn:
      minn = fgon[i][0]
      minnx = i
  sol = ""
  for i in range(5):
    sol += "".join([str(x) for x in fgon[(minnx+i)%5]])
  return int(sol)

def gen():
  for perm in permutations(nums):
    attempt = [perm[0:3]]
    for i in range(1, 5):
      if i != 4:
        attempt.append( (perm[1 + 2*i], attempt[i-1][2], perm[1 + 2*i + 1]) )
      else: 
        attempt.append( (perm[1 + 2*i], attempt[i-1][2], attempt[0][1]) )
    if isValid(attempt):
      sol = solSet(attempt)
      if len(str(sol)) == 16:
        yield sol



print(max([x for x in gen()]))
    
