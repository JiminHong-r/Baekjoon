import sys

k = int(sys.stdin.readline())

for i in range(k):
    lst = list(map(int, sys.stdin.readline().split()))
    del lst[0]
    gap = []
    print("Class", i + 1)
    print("Max", max(lst), end=', ')
    print("Min", min(lst), end=', ')
    lst.sort(reverse=True)
    for j in range(len(lst) - 1):
        gap.append(lst[j] - lst[j + 1])
    print("Largest gap", max(gap))