c = [200, 100, 50, 20, 10, 5, 2, 1]

count = 0
for c200 in range(0, 201, 200):
  for c100 in range(0, 201-c200, 100):
    for c50 in range(0, 201-c200-c100, 50):
      for c20 in range(0, 201-c200-c100-c50, 20):
        for c10 in range(0, 201-c200-c100-c50-c20, 10):
          for c5 in range(0, 201-c200-c100-c50-c20-c10, 5):
            for c2 in range(0, 201-c200-c100-c50-c20-c10-c5, 2):
              count += 1

print(count)