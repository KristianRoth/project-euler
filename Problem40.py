






def get(n):
  count = 0
  for num in range(1, 1000000):
    for i in str(num):
      count += 1
      if count in n:
        n.remove(count)
        if len(n) == 0:
          return i
        yield i

product = 1
for i in get([1, 10, 100, 1000, 10000, 100000, 1000000]):
  product *= int(i)
  print(i)

print(product)