from math import sqrt
a = 1
b = 0
while a < 334:
    b = a + 1
    while b < 500:
        c = sqrt(a * a + b * b)
        if a + b + c == 1000:
            print(a*b*c)
            exit()
        b += 1
    a += 1
