from collections import deque

n = int(input())
c = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(c):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (n + 1)
cnt = []

def dfs(graph, v, visited):
    visited[v] = 1
    cnt.append(v)
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i]:
            dfs(graph, i, visited)
            
dfs(graph, 1, visited)
print(len(cnt) - 1)