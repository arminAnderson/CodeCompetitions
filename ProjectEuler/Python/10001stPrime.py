from math import sqrt

def IsPrime(num):
    if num % 2 == 0:
        return False
    i = 3
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 2
    return True

num = int(input())
sum = 0
i = 0

while sum != num:
    if IsPrime(i):
        sum += 1
    i += 1
print(i - 1)