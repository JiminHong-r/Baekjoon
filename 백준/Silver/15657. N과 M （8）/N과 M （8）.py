n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = []

def dfs(start, visited):
    if (len(visited) == m):
        print(' '.join(map(str, visited)))
        return
    for i in range(start, n):
        visited.append(num[i])
        dfs(i, visited)
        visited.pop()
        
dfs(0, visited)