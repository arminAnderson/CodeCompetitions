def Factors(num):
    sum = 1
    i = 2
    while i * i < num:
        if num % i == 0:
            sum += i + num/i
        i += 1
    if i * i == num:
        sum += i
    return int(sum)

abNum = []
arr = [0] * 28124

for i in range(1, 28124):
    if i < Factors(i):
        abNum.append(i)
 
i = 0
j = 0
while i < len(abNum):
    while j < len(abNum):
        if abNum[i] + abNum[j] < 28124:
            arr[abNum[i] + abNum[j]] = 1
        j += 1
    i += 1
    j = i

sum = 0
for i in range(1, 28124):
    if arr[i] == 0:
        print(i)
        sum += i
print(sum)

