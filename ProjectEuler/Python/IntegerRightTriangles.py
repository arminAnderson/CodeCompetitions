most = 0
m = 0
index = 0
for p in range(1001):
    m = 0
    for a in range(1, p//3 + 1):
        for b in range(a, p//2 + 1):
            c = p - a - b
            if a + b + c == p and a * a + b * b == c * c:
                m += 1
    if m > most:
        index = p
        most = m

print("{} {}".format(index, most))


    