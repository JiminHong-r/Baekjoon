n = int(input())

info = []
for i in range(n):
    key, name = map(str, input().split())
    info.append([int(key), name])

info.sort(key=lambda x : x[0])
for i in info:
    print(i[0], i[1])