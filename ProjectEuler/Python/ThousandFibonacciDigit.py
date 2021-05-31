a = 1
b = 1
c = 0
temp = 0
pos = 1

while c < 1000:
    temp = a
    a = b
    b += temp

    num = temp
    c = 0
    while num > 0:
        c += 1
        num //= 10

    print("{} : {} : {}".format(temp, pos, c))
    pos += 1

print(sum)