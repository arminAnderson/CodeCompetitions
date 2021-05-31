f = open("inputFiles/LargeSum.txt", "r")
sum = 0
for line in f.readlines():
    sum += int(line)
    print(sum)

s = sum
count = 0
while s > 0:
    s //= 10
    count += 1

while count - 10 > 0:
    sum //= 10
    count -= 1

print(sum)
