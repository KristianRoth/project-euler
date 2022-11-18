def good(n):
  return str(n) == str(n)[::-1] and "{0:b}".format(n) == "{0:b}".format(n)[::-1]


summ = 0
for i in range(1, 1000000):
  if good(i):
    summ += i
print(summ)