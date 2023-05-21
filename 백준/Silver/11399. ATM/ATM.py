n = int(input())

p = list(map(int, input().split()))
p.sort()
sum = 0
results = 0
for i in range(n):
    sum += p[i]
    results += sum

print(results)