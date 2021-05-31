from math import sqrt

def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

consec = 4
for i in range(644, 1000000):
    j = 2
    facs = 4
    while j * j <= i:
        if i % j == 0:
            if IsPrime(j):
                facs -= 1
            if facs == 0:
                break
            if IsPrime(i/j):
                facs -=1
            if facs == 0:
                break
        j += 1
    if facs == 0:
        consec -= 1
        if consec == 0:
            print(i)
            exit()
    else:
        consec = 4
