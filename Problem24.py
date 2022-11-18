from itertools import permutations 

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = permutations(nums) 

for i,perm  in enumerate(perms):
  if i >= 1000000-1:
    result = perm
    break

s = ""
for c in result:
  s += str(c)

print(s)