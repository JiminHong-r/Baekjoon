sen = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in sen:
        print(sen.index(i), end=' ')
    else:
        print(-1, end=' ')