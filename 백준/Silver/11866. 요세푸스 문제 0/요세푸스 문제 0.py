from collections import deque

n, k = map(int, input().split())
josep = deque(list(i + 1 for i in range(n)))

res = []
while (josep):
	for _ in range(k - 1):
		josep.append(josep.popleft())
	res.append(str(josep.popleft()))

print('<' + ', '.join(res) + '>')

