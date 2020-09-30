checker = set()
def GeneratePentNums():
    s = []
    for i in range(1,1000001):
        val = int(i * (3 * i - 1)/2)
        s.append(val)
        checker.add(val)
    return s

pent = GeneratePentNums()
print(92 in checker)

for a in range(1000):
    for b in range(a, 1000):
        if pent[a] + pent[b] in checker and pent[b] - pent[a] in checker:
            print("{} {}".format(a, b))