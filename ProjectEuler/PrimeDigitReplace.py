arr = []
def Increment(numArr):
    i = len(numArr) - 1
    numArr[i] += 1
    while(numArr[i] > 9):
        numArr[i] = 0
        i -= 1
        if i < 0:
            break
        numArr[i] += 1

def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

for i in range(5, 6):
    arr.clear()
    for j in range(10):
        arr.append([1] + [0] * (i - 1))
    replacementDigit = 0
    replacementCount = 2
    while arr[0][0] != 0:
        for 

print(arr)