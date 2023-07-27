import sys
from collections import Counter

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for i in range(n)]
avg = round(sum(num) / n)
print(avg)

num.sort()
mid = num[n // 2]
print(mid)

cnt = Counter(num).most_common()
if (len(cnt) > 1 and cnt[0][1] == cnt[1][1]):
	print(cnt[1][0])
else:
	print(cnt[0][0])

ran = max(num) - min(num)
print(ran)
