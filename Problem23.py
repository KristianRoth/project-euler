import time
start_time = time.time()
upper = 28123

def primeFactors(n, first = True):
  for i in range(2, (n**1/2)+1):
    if n%i==0:
      return [i] + primeFactors(n/i, False)
  if first:
    return []
  return [n]


def sumOfFactors(n):
  primes = primeFactors(n)




# def sumOfFactors(n):
#   return sum([i for i in range(1, (n**1/2)+1) if n%i==0])

# numbers = [i for i in range(1, upper+1) if i < sumOfFactors(i)]

# print(time.time() - start_time)

# sums = []

# for num1 in numbers:
#   for num2 in numbers:
#     if (num2 >= num1):
#       s = num1 + num2
#       if s > (upper+1):
#         break
#       else:
#         sums.append( s )

# summ = sum(set(sums))

# print(sum(range(1, upper+2)) - summ) #4179871

# print(time.time() - start_time)