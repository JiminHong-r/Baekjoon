n = int(input())

A = list(map(int, input().split()))
P = []
for i in range(n):
    P.append(0)

idx = 0
for i in range(n):
    minidx = A.index(min(A))
    A[minidx] = max(A) + 1
    P[minidx] = idx
    idx += 1

for i in range(n):
    print(P[i], end=' ')