import sys
from collections import Counter

n = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))

cnt = Counter(num1)

for i in num2:
    if (i in cnt):
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
