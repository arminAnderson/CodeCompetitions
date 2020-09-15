largest = 0
curr = 1
answer = 0
for i in range(1000000):
    if i == 0:
        continue
    num = i
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        curr += 1
    if curr > largest:
        largest = curr
        answer = i
    curr = 1

print(answer)