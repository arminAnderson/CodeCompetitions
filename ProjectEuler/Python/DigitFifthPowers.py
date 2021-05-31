def GetPowerSum(num):
    sum = 0
    while num > 0:
        sum += (num % 10) ** 5
        num //= 10
    return sum

sum = 0
for i in range(2, 1000000):
    if i == GetPowerSum(i):
        sum += i

print(sum)