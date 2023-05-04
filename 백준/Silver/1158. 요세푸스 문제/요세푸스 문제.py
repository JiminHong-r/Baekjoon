n, k = map(int, input().split())

q = []
s = []

for i in range(n):
	q.append(i + 1)

idx = k - 1
for i in range(len(q)):
	if (len(q) > idx):
		s.append(q.pop(idx))
		idx += k - 1
	else:
		idx %= len(q)
		s.append(q.pop(idx))
		idx += k - 1

print("<", end ='')
for i in range(n):
	if (i < n - 1):
		print(s[i], end=', ')
	else:
		print(s[i], end='')
print(">")