def SumOfSquares(num):
    sum = 0
    for i in range(num + 1):
        sum += i * i
    return sum

def SquareOfSum(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum * sum

num = int(input())
print(SquareOfSum(num) - SumOfSquares(num))