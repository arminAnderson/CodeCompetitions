def DigitCount(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return(count)

prev_t = 1
prev_b = 0
new_t = 1
new_b = 1

result = 0

for i in range(1000):
    t = new_t * 2 + prev_t
    b = new_b * 2 + prev_b

    if DigitCount(t) != DigitCount(b):
        result += 1

    prev_t = new_t
    prev_b = new_b
    new_t = t
    new_b = b

print(result)