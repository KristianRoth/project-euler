from fractions import Fraction

fl = Fraction(0,1)
fu = Fraction(1,1)
ft = Fraction(3,7)
while True:
  fn = Fraction(fl.numerator + fu.numerator, fl.denominator + fu.denominator)
  if fn < ft:
    fl = fn
  else:
    fu = fn
  print(fl, fu)
  if (fl.denominator > 10**6):
    exit()
