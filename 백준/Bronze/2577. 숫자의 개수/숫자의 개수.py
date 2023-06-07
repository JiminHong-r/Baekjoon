a = int(input())
b = int(input())
c = int(input())

results = list(str(a * b * c))

for i in range(10):
    print(results.count(str(i)))