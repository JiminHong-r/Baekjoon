t = int(input()) # testcase

# nCr n:동 r:서

#def getCombination(n, r):
#    if ((n == r) or (r == 0)):
#        return (1)
#    return (getCombination(n - 1, r - 1) + getCombination(n - 1, r))

def factorial(n, r):
    if (n == r):
        return (r)
    return (n * factorial(n - 1, r))

for i in range(t):
    r, n = map(int, input().split())
    print(int(factorial(n, n - r + 1) / factorial(r, 1)))