def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for i in range(9, 10000, 2):
    found = False
    if not IsPrime(i):
        j = 1
        while(j * j * 2 <= i):
            s = j * j * 2
            p = i - s
            found = IsPrime(p)
            if found:
                print("{} {} {}".format(i, p, j))
                break
            j += 1
        if not found:
            print("INVALID: " + str(i))
            exit()