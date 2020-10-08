num = 0
for i in range(1, 1001):
    num += i ** i

ret = 0
for i in range(10):
    ret *= 10
    ret += num % 10
    print(num % 10)
    num //= 10
print(ret)