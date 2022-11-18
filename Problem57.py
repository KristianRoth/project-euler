from fractions import Fraction


f = Fraction(1,2)
c = 0
for i in range(1000):
  f1 = f + 1
  if len(str(f1.numerator)) > len(str(f1.denominator)):
    c += 1
  f = Fraction(1,2+f)
print(c)