t = int(input())

for i in range(t):
    info = list(map(str, input().split()))
    r = int(info[0])
    s = info[1]
    for i in range(len(s)):
        print(s[i] * r, end='')
    print()