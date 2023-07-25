n = int(input())

big = []

for i in range(n):
	weight, height = map(int, input().split())
	big.append([weight, height])

for i in big:
	rank = 1
	for j in big:
		if (i[0] < j[0] and i[1] < j[1]):
			rank += 1
	print(rank)