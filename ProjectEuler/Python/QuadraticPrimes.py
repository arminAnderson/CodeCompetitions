cache = [1] * 150001

i = 2
j = -1
while i <= 150000:
    j = i + i
    while j <= 150000:
        cache[j] = 0
        j += i
    i += 1

#for i in range(1, 11):
#    print("{} prime? {}".format(i, cache[i]))

print("Starting program...")

longest = 0
_a = 0
_b = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        sum = 0
        for n in range(100):
            if cache[abs((n * n) + (a * n) + b)] == 1:
                sum += 1
            else:
                break
        if sum > longest:
            longest = sum
            _a = a
            _b = b

print(longest)
print("{}, {}, {}".format(longest, _a, _b))
