mel = list(map(int, input().split()))

if (mel == sorted(mel)):
    print("ascending")
elif (mel == sorted(mel, reverse=True)):
    print("descending")
else:
    print("mixed")