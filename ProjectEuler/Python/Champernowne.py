irrational = ""

i = 1
while len(irrational) < 1000000:
    irrational += str(i)
    i += 1

result = 1
multi = 1

for i in range(7):
    print(multi)
    result *= int(irrational[multi-1])
    multi *= 10

print(result)