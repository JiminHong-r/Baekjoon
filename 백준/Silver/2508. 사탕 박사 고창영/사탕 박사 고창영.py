import sys

t = int(input())

for i in range(t):
	cnt = 0
	sys.stdin.readline()
	r, c = map(int, input().split())
	candy = [list(map(str, input())) for _ in range(r)]
	for j in range(r):
		for k in range(c - 2):
			if (candy[j][k] == ">" and candy[j][k + 1] == "o" and candy[j][k + 2] == "<"):
				cnt += 1
	for j in range(r - 2):
		for k in range(c):
			if (candy[j][k] == "v" and candy[j + 1][k] == "o" and candy[j + 2][k] == "^"):
					cnt += 1
	print(cnt)