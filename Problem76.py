# Wolfram
# series expansion (product (1-x^k)^(-1), k=1..99)
# cofficient of x^100

list = [1] + [0] * 100
for coin in range(1, 100):
	for i in range(coin, 100+1):
		list[i] += list[i - coin]
print(list[100])