num = int(input())
sum = 0

for i in range(num):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
