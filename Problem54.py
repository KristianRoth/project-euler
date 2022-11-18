
num = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["S", "D", "C", "H"]

def hands():
  with open("p054_poker.txt", "r") as poker:
    for hand in poker:
      one = hand[0:14]
      two = hand[15:-1]
      yield (one.split(" "), two.split(" "))

def straitFlush(hand):
  return flush(hand) and strait(hand)

def flush(hand):
  for s in suits:
    f = True
    for card in hand:
      if s not in card:
        f = False
        continue
    if f:
      return high(hand)
  return False

def numInHand(hand, i):
  for card in hand:
    if i in card:
      return True
  return False

def strait(hand):
  for start in range(len(num)-4):
    f = True
    for i in range(start, start+5):
      if not numInHand(hand, num[i]):
        f = False
        continue
    if f:
      return i
  return False

def count(hand, i):
  count = 0
  for card in hand:
    if i in card:
      count += 1
  return count

def same(hand, n):
  for i in range(len(num)):
    if count(hand, num[i]) == n:
      return i
  return False

def twoPair(hand):
  f = False
  for i in range(len(num)):
    if count(hand, num[i]) == 2:
      if f:
        return i
      f = True
  return False

def four(hand):
  return same(hand, 4)

def three(hand):
  return same(hand, 3)

def pair(hand):
  return same(hand, 2)

def fullHouse(hand):
  return same(hand, 2) and same(hand, 3)

def high(hand):
  for i in reversed(range(len(num))):
    for card in hand:
      if num[i] in card:
        return i

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
funs = [straitFlush, straitFlush, four, fullHouse, flush, strait, three, twoPair, pair]

def oneWins(game, f = 0):
  one = funs[f](game[0])
  two = funs[f](game[1])
  if one and two:
    return one > two
  if one and not two:
    print("One wins", funs[f].__name__)
    return True
  if not one and two:
    print("Two wins", funs[f].__name__)
    return False
  if not one and not two:
    if f == len(funs) - 1:
      return high(game[0]) > high(game[1])
    return oneWins(game, f+1)

c = 0
for game in hands():
  if oneWins(game):
    c += 1

print(c)


