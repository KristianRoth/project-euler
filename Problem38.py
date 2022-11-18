def getDigits(n):
  return [int(x) for x in str(n)]

def generateCandidates(candidates = ["9"]):
  ncandidates = []
  for c in candidates:
    for i in range(8, 0, -1):
      ncandidates.append(c+str(i))
      yield c+str(i)
  for i in generateCandidates(ncandidates):
    yield i

def test(candidate):
  for i in range(1, 5):
    pandigital = ""
    for j in range(1, i + 2):
      # print(str(candidate) + "*" + str(j) + " = " + str(candidate*j))
      pandigital += str(candidate*j)
      if len(pandigital) > 9:
        return False

    ispandigital = True
    for i in "123456789":
      if i not in pandigital:
        ispandigital = False
    
    if ispandigital:
      print(j)
      print(candidate)
      print(pandigital)
      exit()

for c in generateCandidates():
  candidate = int(c)
  test(candidate)
