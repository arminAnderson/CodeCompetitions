import math

def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def GetCorners(root):
    base = root * root
    arr = [0] * 4
    arr[0] = base
    arr[1] = base + 1 - root
    arr[2] = base + 2 - root * 2
    arr[3] = base + 3 - root * 3
    return arr

primes = 0
total = 1
side = 1

for i in range(3, 1000000, 2):
    corners = GetCorners(i)
    total += 4
    side += 1
    for corner in corners:
        if IsPrime(corner):
            primes += 1
    if primes/total < .1:
        print(i)
        exit()
