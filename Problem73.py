from util import farey_sequence
from fractions import Fraction



lower = Fraction(1, 3)
upper = Fraction(1, 2)

c = 0
count = 0
for x in farey_sequence(12000):
  c += 1
  if c%10000 == 0:
    print(c, float(x))
  if lower < x:
    if upper <= x:
      break
    count += 1

print(count)