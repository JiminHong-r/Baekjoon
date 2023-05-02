n, m = map(int, input().split()) # 끊어진 기타줄 개수 / 브랜드
Six = []
One = []

for i in range(m):
    six, one = map(int, input().split())
    Six.append(six)
    One.append(one)
    if ((n // 6 + 1) * min(Six) < n * min(One)):
        if (n % 6 == 0):
            price = (n // 6) * min(Six)
        else:
            price = (n // 6 + 1) * min(Six)
    elif (n // 6) * min(Six) + (n % 6) * min(One) < n * min(One):
        price = (n // 6) * min(Six) + (n % 6) * min(One)
    else:
        price = n * min(One)

print(price)