sen = input()

up = sen.upper()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cnt = [0] * len(alphabet)

for i in range(len(alphabet)):
    if alphabet[i] in up:
        for j in range(len(up)):
            if (alphabet[i] == up[j]):
                cnt[i] += 1

check = 0
for i in range(len(cnt)):
    m = max(cnt)
    if (cnt[i] == m):
        check += 1
        alpha = alphabet[i]
        
if (check < 2):
    print(alpha)
else:
    print("?")