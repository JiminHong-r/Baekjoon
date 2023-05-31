n, m = map(int, input().split())
visited = []

def nandm(visited, start):
    if (len(visited) == m):
        print(' '.join(map(str, visited)))
        return
    for i in range(start, n + 1):
        visited.append(i)
        nandm(visited, i)
        visited.pop()

nandm(visited, 1)