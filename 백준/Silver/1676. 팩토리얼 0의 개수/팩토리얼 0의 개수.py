import sys

n = int(sys.stdin.readline())

def factorial(n):
	if (n == 0):
		return 1
	elif (n == 1):
		return 1
	else:
		return n * factorial(n - 1)

num = str(factorial(n))
cnt = 0

for i in num[::-1]:
	if (i == '0'):
		cnt += 1
	else:
		break

print(cnt)