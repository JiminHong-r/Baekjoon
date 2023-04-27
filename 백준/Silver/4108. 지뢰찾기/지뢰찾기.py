dx = [-1, -1, -1, 0, 1, 1, 1, 0] # 상하좌우대각선 오돌
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def init():
	for i in range(r):
		col = input()
		for j in range(c):
			if (col[j] == '.'):
				bomb[i].append(0)
			else:
				bomb[i].append('*')

while (1):
	r, c = map(int, input().split())
	if ((r == 0) and (c == 0)):
		break
	bomb = [[] for _ in range(r)]
	init()
	for x in range(len(bomb)):
		for y in range(len(bomb[x])):
			if (bomb[x][y] == '*'):
				for i in range(8):
					nx = x + dx[i]
					ny = y + dy[i]
					if (0 <= nx < r and 0 <= ny < c and bomb[nx][ny] != '*'):
						bomb[nx][ny] += 1
	for i in range(r):
		for j in range(c):
			print(bomb[i][j], end='')
		print(end="\n")