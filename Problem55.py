
def lychrel(n, count = 0):
  if (count >= 50):
    return False
  n2 = n + int(str(n)[::-1])
  if str(n2) == str(n2)[::-1]:
    # print(n2)
    return True
  return lychrel(int(n2), count + 1) 




c = 0
for i in range(1,10000):
  if not lychrel(i):
    c += 1
print(c)