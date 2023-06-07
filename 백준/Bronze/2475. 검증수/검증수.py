num = list(map(int, input().split()))

for i in range(len(num)):
    num[i] = num[i] * num[i]
    
n = sum(num) % 10
print(n)