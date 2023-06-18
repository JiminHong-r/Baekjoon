n = int(input())
x = list(map(int, input().split()))

lst = []
for i in x:
    if i == 1:
        lst.append(i)
       
    for j in range(2, i - 1):
        if (i % j == 0):
            lst.append(i)
            break

print(len(x) - len(lst))