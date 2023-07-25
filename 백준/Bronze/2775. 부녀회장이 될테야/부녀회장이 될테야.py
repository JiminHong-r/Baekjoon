t = int(input())

for i in range(t):
	k = int(input())
	n = int(input())
	building = [i for i in range(1, n + 1)]
	for j in range(k):
		for l in range(1, n):
			building[l] += building[l - 1]
	print(building[-1])
