def IsPalindrome(num):
    return num == Reverse(num)

def Reverse(num):
    flip = 0
    while num > 0:
        flip *= 10
        flip += num % 10
        num //= 10
    return flip

count = 0
pal = False
for i in range(1, 10000):
    pal = False
    for j in range(50):
        i += Reverse(i)
        if IsPalindrome(i):
            pal = True
            break
    if not pal:
        count += 1

print(count)
        