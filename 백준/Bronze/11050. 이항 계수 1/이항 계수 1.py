n, k = map(int, input().split())

def factorial(n, k):
	res = 1
	for i in range(n - k + 1, n + 1):
		res *= i
	return res

print(factorial(n, k) // factorial(k, k))