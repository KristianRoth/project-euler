from util import sumOfFactorial


loops = dict()

c = 0
idd = 1
for n in range(1, 10**6):
  c += 1
  if c%1000 == 0:
    print(c)
  numbers = []
  prev = 0
  while n not in numbers:
    if n in loops:
      prev = loops[n]
      break
    numbers.append(n)
    n = sumOfFactorial(n)
  lenn = len(numbers)
  loopLen = (len(numbers) - (numbers.index(n) + 1)) if n in numbers else 0
  for num in numbers:
    loops[num] = loopLen if lenn <= loopLen else lenn + prev
    lenn -= 1


print(len(list(filter(lambda x: x == 60, loops.values()))))