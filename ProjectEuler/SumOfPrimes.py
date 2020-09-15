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
    
sum = 2

i = 3
while i < 10:
    if IsPrime(i):
        sum += i
    i += 2

print(sum)