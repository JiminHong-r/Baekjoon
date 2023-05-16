t = int(input())

for i in range(t):
    vps = input()
    cnt = 0
    stack = []
    for j in vps:
        if (j == '('):
            stack.append(j)
        elif (j == ')'):
            if (len(stack) == 0):
                cnt += 1
            else:
                stack.pop()

    if (len(stack) == 0) and (cnt == 0):
        print("YES")
    else:
        print("NO")