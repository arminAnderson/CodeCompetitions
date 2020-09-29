from math import factorial

def FactorialSum(num):
    s = 0
    n = num
    while n > 0:
        s += factorial(n % 10)
        n //= 10
    return s == num

answer = 0
for i in range(3,1000000):
    if FactorialSum(i):
        answer += i
print(answer)