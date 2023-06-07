num = []
mol = []
for i in range(10):
    num.append(int(input()))
for i in range(10):
    mol.append(num[i] % 42)
    
print(len(set(mol)))