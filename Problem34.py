import math

def getDigits(n):
  return [int(x) for x in str(n)]

def getSum(n):
  return sum([math.factorial(i) for i in getDigits(n)])

summ = 0
for i in range(3, 100000):
  if i == getSum(i):
    print(i)
    summ += i
print(summ)