x = int(input()) # 64보다 작거나 같은 자연수
n = 64
cnt = 0

while x > 0:
    if n > x:
        n = n // 2
    else:
        cnt += 1
        x -= n

print(cnt)