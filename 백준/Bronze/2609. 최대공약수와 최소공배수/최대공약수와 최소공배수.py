a, b = map(int, input().split())

def gcd(a, b):
	mod = a % b
	if (mod == 0):
		return b
	return gcd(b, mod)

print(gcd(a, b))
print(a * b // gcd(a, b))