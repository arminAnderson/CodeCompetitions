num = int(input())

a = 1
b = 2
temp = 0
sum = 0

while b < num:
    if b % 2 == 0:
        sum += b
    temp = a
    a = b
    b += temp

print(sum)
