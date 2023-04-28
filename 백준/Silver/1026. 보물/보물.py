n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortedA = sorted(A)
sortedB = sorted(B, reverse=True)

# sort: 정렬
# sorted: list 정렬된 결과 반환

sum = 0
for i in range(n):
    sum += sortedA[i] * sortedB[i]
print(sum)