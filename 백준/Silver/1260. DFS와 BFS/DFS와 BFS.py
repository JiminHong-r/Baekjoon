from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
	x, y = map(int, input().split())
	graph[x][y] = 1
	graph[y][x] = 1

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

def dfs(graph, v, visited1):
	visited1[v] = 1
	print(v, end=" ")
	for i in range(1, n + 1):
		if not visited1[i] and graph[v][i]:
			dfs(graph, i, visited1)

def bfs(graph, v, visited2):
	queue = deque([v])
	visited2[v] = 1
	while (queue):
		v = queue.popleft()
		print(v, end=" ")
		for i in range(1, n + 1):
			if not visited2[i] and graph[v][i]:
				queue.append(i)
				visited2[i] = 1

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)