def IsPalindrome(num):
    if num % 10 == 0:
        return False
    flip = 0
    og = num
    while num > 0:
        flip *= 10
        flip += num % 10
        num //= 10
    return og == flip

result = 0
for i in range(1, 1000000):
    if IsPalindrome(i) and IsPalindrome(int(bin(i)[2:])):
        result += i
print(result)