def IsPalindrome(num):
    flip = 0
    og = num
    while num > 0:
        flip *= 10
        flip += num % 10
        num //= 10
    return og == flip

i = 999
j = 999
largest = 0

while i > 99:
    while j > 99:
        if IsPalindrome(i * j):
            if largest < i * j:
                largest = i * j
        j -= 1
    i -= 1
    j = i

print(largest)
    
