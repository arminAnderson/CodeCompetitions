def SumDigits(num):
    ret = 0
    while num > 0:
        ret += num % 10
        num //= 10
    return ret

largest = 0
for a in range(100):
    for b in range(100):
        largest = max(largest, SumDigits(a**b))
print(largest)