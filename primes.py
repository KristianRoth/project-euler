import sys
import math
import os
import time

this = sys.modules[__name__]
this.primeSet = None
this.primeList = None

def _makeSet():
  primes = []
  print("Making prime set")
  with open("primelist.txt", 'r') as primelist:
    for line in primelist:
      primes.append(int(line))
  this.primeList = primes
  this.primeSet = set(primes)
  print("Prime set DONE")
  
_makeSet()

def primes(a = 0, b = 10000000):
  p1 = this.primeList[0]
  for p in this.primeList:
    if (p > b):
      return p1
    p1 = p
    if (p < a):
      continue
    yield p1
    


def factors(n, start = 2):
  if n == 1:
    return []
  sq = int(math.sqrt(n) + 1)
  for p in primes(start, sq):
    if n%p == 0:
      return factors(n//p, p) + [p]
  return [n]

def divisors(n):
  if isPrime(n):
    return [1, n]
  if n == 1:
    return [1]
  divisors = [1]
  for i in range(2, n + 1):
    if n%i == 0:
      divisors.append(i)
  return divisors

def totient(n):
  if (isPrime(n)):
    return n-1
  t = n
  for p in set(factors(n)):
    t *= (1-1.0/p)
  return int(t)

def isPrime(n):
  if n > 10**7:
    return isPrimeC(n)    
  return n in this.primeSet


def _isPrime(n):
  if n == 1:
    return False
  sq = int(math.sqrt(n) + 1)
  for i in range(2, sq):
    if n%i == 0:
      return False
  return True

def isPrimeC(n):
  if n > 10**14:
    raise Exception("Too fuckin big n: " + str(n))
  sq = int(math.sqrt(n) + 1)
  for i in primes():
    if i > sq:
      break
    if n%i == 0:
      return False
  return True


def _calPrimes(n):
  for p in range(2, n):
    if _isPrime(p):
      yield p


def _calPrimes2():
  for p in range(1000000, 10000000):
    if isPrimeC(p):
      yield p

def genPrimes():
  start_time = time.time()
  
  print("Starting generating primes")
  with open("primelist2.txt", "a") as primelist:
    for p in _calPrimes2():
      primelist.write(str(p) + os.linesep)
  print("Generated primes. It took: " + str(time.time() - start_time) + "s")