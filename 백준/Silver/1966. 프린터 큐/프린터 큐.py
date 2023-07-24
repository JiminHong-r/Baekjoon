from collections import deque

priority = deque()

t = int(input())

for i in range(t):
	n, m = map(int, input().split())
	priority = deque(list(map(int, input().split())))
	idx = deque(list(priority))
	idx[m] = 10
	rank = 0
	while priority:
		if (priority[0] == max(priority)):
			rank += 1
			if (idx[0] == 10):
				print(rank)
				break
			priority.popleft()
			idx.popleft()
		else:
			priority.append(priority.popleft())
			idx.append(idx.popleft())