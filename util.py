from fractions import Fraction
import math

def farey_sequence(n, descending = False):
    (a, b, c, d) = (0, 1, 1, n)
    if descending:
        (a, c) = (1, n - 1)
    yield Fraction(a, b)
    while (c <= n and not descending) or (a > 0 and descending):
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        yield Fraction(a, b)

def getDigits(n):
  return [int(x) for x in str(n)]

def getNumber(digits):
  return int("".join([str(x) for x in digits]))

def sumOfFactorial(n):
  return sum([math.factorial(x) for x in getDigits(n)])