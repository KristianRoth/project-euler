import time
start_time = time.time()

numss = []
with open("triangle.txt", "r") as triangle:
  for line in triangle:
    numss.append([int(x) for x in line.split(" ")])

for i in range(len(numss)-2, -1, -1):
  for pos, num in enumerate(numss[i]):
    numss[i][pos] += max(numss[i+1][pos], numss[i+1][pos+1])
    
print(numss[0][0])

print(time.time() - start_time)