import csv
with open('names.txt') as csvfile:
  names = csv.reader(csvfile).next()

names.sort()

def score(i, name):
  return (i+1) * sum([(ord(x)-64) for x in name])

sum = sum([score(i, name) for i,name in enumerate(names)])
print(sum)