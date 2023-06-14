while (True):
    n = list(input())
    a = reversed(n)
    if (n[0] == '0'):
        break
    if (n == list(a)):
        print('yes')
    else:
        print('no')