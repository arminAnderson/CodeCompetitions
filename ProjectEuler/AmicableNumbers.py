from math import sqrt

def SumOfDiv(num):
    if num == 1: 
        return 0
    sum = 1
    i = 2
    num_sqrt = sqrt(num)
    while i < num_sqrt:
        if num % i == 0:
            sum += i + num/i
        i += 1
    if num % num_sqrt == 0:
        sum += num_sqrt
    return int(sum)

sum = 0
for i in range(2, 10000):
    j = SumOfDiv(i)
    if SumOfDiv(j) == i and i != j:
        sum += i
        print("{}, {}".format(i, j))
print(sum)