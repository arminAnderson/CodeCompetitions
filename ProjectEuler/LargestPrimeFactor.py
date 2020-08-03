from math import sqrt

def IsPrime(num):
    if num % 2 == 0:
        return 0
    i = 3
    while i <= sqrt(num):
        if num % i == 0:
            return 0
        i += 2
    return num
    
num = int(input())
largest = 0

i = 2
while i <= sqrt(num):
    if num % i == 0:
        largest = max(IsPrime(i), IsPrime(num/i))
    i += 1

print(int(largest))
    




