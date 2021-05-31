def HasDigits(ref, target):
    s = set()
    while ref > 0:
        s.add(ref % 10)
        ref //= 10
    size = len(s)
    while target > 0:
        s.add(target % 10)
        target //= 10
        if len(s) > size:
            return False
    return True


for i in range(1,1000000):
    FOUND = True
    for j in range(2, 7):
        if not HasDigits(i, i * j):
            FOUND = False
            break
    if FOUND:
        print(i)
        exit()