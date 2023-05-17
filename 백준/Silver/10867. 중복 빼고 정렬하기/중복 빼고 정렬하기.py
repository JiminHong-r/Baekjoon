n = int(input())

ar = list(map(int, input().split()))
ar = list(set(ar))
ar.sort()

for i in ar:
    print(i, end=' ')