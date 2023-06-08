n = int(input())

coordinate = []
for i in range(n):
    x, y = list(map(int, input().split()))
    coordinate.append([x, y])
coordinate.sort(key=lambda x : (x[0], x[1]))

for i in range(n):
    print(coordinate[i][0], coordinate[i][1])