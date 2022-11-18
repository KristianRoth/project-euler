maxx = 0
for a in range(1, 100):
  for b in range(1, 100):
    summ = sum([int(x) for x in str(a**b)])
    if summ > maxx:
      maxx = summ
print(maxx)