n, m = map(int, input().split())

s = [input() for _ in range(n)]
sen = [input() for _ in range(m)]

cnt = 0
for i in sen:
    if i in s:
        cnt += 1
        
print(cnt)