n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

A.sort()
 
def binary_search(A, target):
	left = 0
	right = len(A) - 1

	while left <= right:
		mid = (left + right) // 2
		if A[mid] == target:
			return 1
		elif A[mid] > target:
			right = mid - 1
		elif A[mid] < target:
			left = mid + 1
	return 0

for i in range(m):
	if (binary_search(A, B[i])):
		print(1)
	else:
		print(0)