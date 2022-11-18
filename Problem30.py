

def getSum(n):
  sum = 0
  for i in str(n):
    sum += int(i)**5
  return sum

n = 10
sum = 0
while True:
  n += 1
  if (n == getSum(n)): 
    sum += n
    print("Num: " + str(n) + " Sum: " + str(sum))