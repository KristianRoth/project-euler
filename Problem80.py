from decimal import *
from util import getDigits
import math
getcontext().prec = 2000
summ = 0
for i in range(1, 1000):
  if not math.sqrt(i).is_integer():
    dec = str(Decimal(i).sqrt()).replace(".", "")
    summ += sum(getDigits(dec[0:1000]))
print(summ)