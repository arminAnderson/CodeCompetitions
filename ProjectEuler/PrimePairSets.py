from math import log
def GetConcats(a, b, c, d, e):
    init = [a, b, c, d, e]
    for i in range(5):
        for j in range(i + 1, 5):
            if primelist[10**int(log(init[j], 10)+1)*init[i]+init[j]] == 0:
                return 0
            if primelist[10**int(log(init[i], 10)+1)*init[j]+init[i]] == 0:
                return 0
    return 1

SIZE = 1000000
primelist = [1] * SIZE
primelist[0] = 0
primelist[1] = 0
i = 2
primesOnly = []
while i < SIZE:
    if primelist[i] == 1:
        primesOnly.append(i)
        j = i * 2
        while j < SIZE:
            primelist[j] = 0
            j += i
    i += 1

smallestSum = 1000000
LIMIT = 700
length = len(primesOnly)

i = 0
while primesOnly[i] < LIMIT:
    i += 1
length = i - 1

print("{} {}".format(length, length ** 5))

a = 0
b = 0
c = 0
d = 0
e = 0

while a < length and primesOnly[a] * 5 < smallestSum:
    b = a + 1
    while b < length and primesOnly[a] + primesOnly[b] * 4 < smallestSum:
        c = b + 1
        while c < length and primesOnly[a] + primesOnly[b] + primesOnly[c] * 3 < smallestSum:
            d = c + 1
            while d < length and primesOnly[a] + primesOnly[b] + primesOnly[c] + primesOnly[d] * 2 < smallestSum:
                e = d + 1
                while e < length and primesOnly[a] + primesOnly[b] + primesOnly[c] + primesOnly[d] + primesOnly[e] < smallestSum:
                    e += 1
                    #print("{} {} {} {} {}".format(a, b, c, d, e))
                    #if GetConcats(primesOnly[a], primesOnly[b], primesOnly[c], primesOnly[d], primesOnly[e]) > 0:
                    #    smallestSum = primesOnly[a] + primesOnly[b] + primesOnly[c] + primesOnly[d] + primesOnly[e]
                    #    print(smallestSum)
                d += 1
            c += 1
        b += 1
    a += 1
print(smallestSum)
    