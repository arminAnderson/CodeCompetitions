def IsPrime(num):
    if (num % 2 == 0 and num > 2) or num == 1:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

iter = 11
remaining = 11
result = 0
while remaining > 0:
    i = iter
    j = 0
    t = 1
    fail = False
    while i > 0:
        j += t * (i % 10)
        t *= 10
        if not IsPrime(i) or not IsPrime(j):
            fail = True
            break
        i //= 10
    if not fail:
        print(iter)
        remaining -= 1
        result += iter
    iter += 2
    
print(result)
