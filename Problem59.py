def cracked(chars, key):
  return "".join([chr(chars[i] ^ key[i%3]) for i in range(0, len(chars))])

def crackedd(chars, key):
  return sum([chars[i] ^ key[i%3] for i in range(0, len(chars))])



with open("p059_cipher.txt", "r") as file:
  chars = file.read().split(",")
  chars = [int(x) for x in chars]


for i in range(97, 123):
  for j in range(97, 123):
    for k in range(97, 123):
      crack = cracked(chars, [i, j, k]).lower()
      if "the" in crack and "and" in crack and "euler" in crack:
        print(crack)
        print([i, j, k])
        print(crackedd(chars, [i, j, k]))
