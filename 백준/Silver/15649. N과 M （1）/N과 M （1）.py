n, m = map(int, input().split())
visited = []

def dfs(visited):
	if (len(visited) == m):
		print(' '.join(map(str, visited)))
		return
	for i in range(1, n + 1):
		if i not in visited:
			visited.append(i)
			dfs(visited)
			visited.pop()

dfs(visited)