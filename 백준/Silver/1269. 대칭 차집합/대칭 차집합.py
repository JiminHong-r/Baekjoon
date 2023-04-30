a, b = map(int, input().split())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

numa = len(A - B)
numb = len(B - A)

print(numa + numb)