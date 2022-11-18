import time
start_time = time.time()

def sumOfFactors(n):
  return sum([i for i in range(1, n**1/2+1) if n%i==0])
    
result = sum([i for i in range(1, 10000) if i != sumOfFactors(i) and i == sumOfFactors(sumOfFactors(i))])

print(result)

print(time.time() - start_time)