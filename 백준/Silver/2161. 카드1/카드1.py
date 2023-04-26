n = int(input())
card = []
removed = []

for i in range(n):
	card.append(i + 1)

while (len(card) > 1):
	a = card.pop(0)
	removed.append(a)
	b = card.pop(0)
	card.append(b)

for i in removed + card:
	print(i, end=' ')