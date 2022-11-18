
count = 0
for n in range(1, 1000):
  for i in range(1, 1000):
    pw = len(str(i**n))
    if pw == n:
      count += 1
    if pw > n:
      break
print(count)