from math import factorial

count = 0
for n in range(1, 101):
    top = factorial(n)
    for r in range(0, n + 1):
        bottom = factorial(r) * factorial(n - r)
        if top/bottom > 1000000:
            count += 1

print(count)
    