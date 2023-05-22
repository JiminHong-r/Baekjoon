k = int(input())

num = []
cal = 0
for i in range(k):
    n = int(input())
    if (n != 0):
        num.append(n)
    else:
        num.pop()
cal = sum(num)
print(cal)