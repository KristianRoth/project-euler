from primes import isPrimeC

def generator():
  start = 1
  n = 2
  while True:
    for i in range(4):
      start += n
      yield start
    n += 2

count = 1
countP = 0
for i in generator():
  count += 1
  if isPrimeC(i):
    countP += 1
  
  if count%4 == 1:
    if (countP / ((count)*1.0) <= 0.10):
      print(i)
      print("Side:", ((count + 4 - count%4)//2)-1)
      print(countP, count)
      exit()

