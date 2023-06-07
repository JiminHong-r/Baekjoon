n = int(input())

for i in range(n):
    pro = input()
    accum = 0
    res = 0
    for i in pro:
        if (i == 'O'):
            accum += 1
            res += accum
        else:
            accum = 0
    print(res)