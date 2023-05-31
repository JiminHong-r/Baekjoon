n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = []

def dfs(visited):
    if (len(visited) == m):
        print(' '.join(map(str, visited)))
        return
    for i in num:
        if i not in visited:
            visited.append(i)
            dfs(visited)
            visited.pop()

dfs(visited)