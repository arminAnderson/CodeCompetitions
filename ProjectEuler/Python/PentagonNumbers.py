checker = set()
s = []
def GeneratePentNums():
    for i in range(1,10001):
        val = int(i * (3 * i - 1)/2)
        s.append(val)
        checker.add(val)
    return s

pent = GeneratePentNums()
print("Generated")

for a in range(10000):
    for b in range(a, 10000):
        if pent[a] + pent[b] in checker and pent[b] - pent[a] in checker:
            print(pent[b] - pent[a])
            exit()