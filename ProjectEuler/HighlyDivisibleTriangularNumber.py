from math import sqrt

def Factors(num):
    count = 0
    i = 1
    max = sqrt(num)
    while i < max:
        if num % i == 0:
            count += 1
        i += 1
    return count * 2

i = 0
length = 0
o = 0

while True:
    length += 1
    i += length
    o = Factors(i)
    if o > 500:
        print(i)
        exit()
    