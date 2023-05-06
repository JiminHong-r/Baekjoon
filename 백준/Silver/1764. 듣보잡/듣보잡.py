n, m = map(int, input().split())

notheard = []
notseen = []

for i in range(n):
	notheard.append(input())
for i in range(m):
	notseen.append(input())

dup = list(set(notheard) & set(notseen))
dup.sort()
print(len(dup))

for i in dup:
	print(i)