# Go to jail square done
# 3 tuplaa G2J done
# CC G2Go and G2J 1/16 done
# CH vituuusti done

from random import randrange, seed
seed(1)

GO = 0
JAIL = 10
G2J = 30
COMMYNITY_CHEST = [2, 17, 33]
CHANCE = [7, 22, 36]
counts = [0]*40

def printCH():
  summ = sum(counts)
  print(" || ".join(["{0:2g} = {1:.3g}%".format(idx, (x/summ)*100) for idx,x in enumerate(counts)]))

def CC(pos):
  rand = randrange(16)
  if rand == 0:
    return GO
  if rand == 1:
    return JAIL
  return pos

def CH(pos):
  rand = randrange(16)
  R = dict({7: 15, 22: 25, 36: 5 })
  U = dict({7: 12, 22: 28, 36: 15})
  M = dict({7:  4, 22: 19, 36: CC(pos)})
  ch = [GO, JAIL, 11, 24, 39, 5, R[pos], R[pos], U[pos], M[pos]]
  if rand < len(ch):
    return ch[rand]
  return pos

def roll():
  d1 = randrange(4)+1
  d2 = randrange(4)+1
  return (d1 + d2, d1 == d2)

pos = 0
doublesc = 0
for i in range(1, 10000000):
  r = roll()
  if r[1]:
    doublesc += 1
  else:
    doublesc = 0
  pos = (pos + r[0]) % 40

  if doublesc == 3:
    pos = JAIL
    doublesc = 0

  if pos == G2J:
    pos = JAIL

  if pos in COMMYNITY_CHEST:
    pos = CC(pos)

  if pos in CHANCE:
    pos = CH(pos)

  counts[pos] += 1

printCH()