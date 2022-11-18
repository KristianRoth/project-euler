import csv

with open('words.txt') as csvfile:
  words = csv.reader(csvfile).next()

def score(name):
  return sum([(ord(x)-64) for x in name])


triangle = []
for i in range(1, 1000):
  triangle.append((i*(i+1))/2)

t = set(triangle)

count = 0
for w in words:
  s = score(w)
  if s in t:
    count += 1

print(count)