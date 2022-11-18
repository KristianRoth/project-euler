months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


days = 0
sundays = 0
for year in range(1901, 2000):
  for mi, n in enumerate(months):
    if (mi == 1):
      if (year%4 == 0 and year%400 != 0):
        days += 1
    days += n
    if (days%7 == 6):
      sundays += 1

print(sundays)