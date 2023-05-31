n, m = map(int, input().split())
visited = []

def nandm(visited):
    if (len(visited) == m):
        print(' '.join(map(str, visited)))
        return
    for i in range(1, n + 1):
        visited.append(i)
        nandm(visited)
        visited.pop()

nandm(visited)