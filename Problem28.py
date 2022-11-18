
starting = 1
sum = 0
for n in range(2, 502):
  starting += 2*(n-1)
  sum += starting
  starting += 2*(n-1)
  sum += starting
  starting += 2*(n-1)
  sum += starting
  starting += 2*(n-1)
  sum += starting
print(sum+1)
