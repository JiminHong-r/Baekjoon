n = int(input())
cnt = 0

def remove_repeated(str):
	result = []
	result.append(str[0])
	for i in range(1, len(str)):
		if (str[i] != str[i - 1]):
			result.append(str[i - 1])
	return (result)
 
for i in range(n):
	str = list(input())
	setstr = set(str)
	str = remove_repeated(str)
	if (len(str) == len(setstr)):
		cnt += 1
print(cnt)