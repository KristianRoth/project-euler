oneToNine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sumOneToNine = sum([len(i) for i in oneToNine])
print(sumOneToNine)
tenToNineteen = len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
sumOnetoNinetyNine = sumOneToNine + tenToNineteen
for ten in tens:
  sumOnetoNinetyNine += len(ten)*10 + sumOneToNine

print(sumOnetoNinetyNine)
sumOneToNineHundredAndNinetyNine = sumOnetoNinetyNine

for hundred in oneToNine:
  sumOneToNineHundredAndNinetyNine += len(hundred + "hundred")
  sumOneToNineHundredAndNinetyNine += len(hundred + "hundredand")*99 + sumOnetoNinetyNine

print(sumOneToNineHundredAndNinetyNine + len("onethousand"))