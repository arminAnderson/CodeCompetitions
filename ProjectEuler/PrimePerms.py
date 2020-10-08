def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for i in range(1001, 10000, 2):
    if IsPrime(i):
        s = set()
        temp = i
        unique = 0
        while temp > 0:
            s.add(temp % 10)
            temp //= 10
        unique = len(s)

        for j in range(1, 3335):
            if i + (2 * j) >= 10000:
                break
            if IsPrime(i + j) and IsPrime(i + (j * 2)):
                invalid = False
                ts = set()

                temp = i + j
                while temp > 0:
                    z = temp % 10
                    if z in s:
                        temp //= 10
                        ts.add(z)
                    else:
                        invalid = True
                        break

                if invalid or len(ts) != unique:
                    continue
                
                ts.clear()
                temp = i + j * 2
                while temp > 0:
                    z = temp % 10
                    if z in s:
                        temp //= 10
                        ts.add(z)
                    else:
                        invalid = True
                        break
                
                if not invalid and len(ts) == unique:
                    print("{} {} {}".format(i, i+j, i+j*2))

