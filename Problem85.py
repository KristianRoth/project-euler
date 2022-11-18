
def countRect(X, x):
  (M, N) = X
  (m, n) = x
  return (M-m+1)*(N-n+1)


def countAll(X):
  (M, N) = X
  summ = 0
  for m in range(1, M+1):
    for n in range(1, N+1):
      summ += countRect(X, (m, n))
  return summ


minn = 2000000
minA = 0


for M in range(1, 1000):
  for N in range(1, M):
    c = countAll((M, N))
    count = abs(c - 2*10**6)
    if count < minn:
      minn = count
      minA = N*M
      print(minn, minA, M, N)
    if c > 2*10**6:
      break

print(minn, minA)