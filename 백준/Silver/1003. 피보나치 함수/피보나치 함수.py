zero = [1, 0, 1]
one = [0, 1, 1]

def dp_fibonacci(n):
	if (len(zero) <= n):
		for i in range(len(zero), n + 1):
			zero.append(zero[i - 1] + zero[i - 2])
			one.append(one[i - 1] + one[i - 2])
	print(zero[n], one[n])

t = int(input())
for i in range(t):
	n = int(input())
	dp_fibonacci(n)