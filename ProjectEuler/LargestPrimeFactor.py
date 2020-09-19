from math import sqrt

def IsPrime(num):
    if num % 2 == 0:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return 0
        i += 2
    return num
    
num = int(input())
largest = 0

i = 2
while i * i <= num:
    if num % i == 0:
        l = max(IsPrime(i), IsPrime(num/i))
        largest = max(largest, l)
    i += 1

print(int(largest))
    




