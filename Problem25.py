
f1 = 1
f2 = 1

for i in range(3, 5000):
  f3 = f1 + f2
  f1 = f2
  f2 = f3
  if i % 100 == 0:
    print(str(i) + ": " + str(len(str(f2))))
  if (len(str(f2)) >= 1000 ):
    print("FIRST OVER 1000: " + str(i) + ": " + str(len(str(f2))))
    break