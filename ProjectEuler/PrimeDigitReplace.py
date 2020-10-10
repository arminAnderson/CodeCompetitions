def Increment(numArr):
    i = len(numArr) - 1
    numArr[i] += 1
    while(numArr[i] > 9):
        numArr[i] = 0
        i -= 1
        if i < 0:
            break
        numArr[i] += 1

def ConvertToNum(list):
    ret = 0
    for i in list:
        ret *= 10
        ret += i
    return ret

def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def Scan(a, depth, alt):
    if depth == len(a):
        return 0
    if IsPrime(ConvertToNum(a)):
        print(a)
        return 1
    b = a
    b[depth] = alt
    return Scan(a, depth + 1, alt) + Scan(b, depth + 1, alt)
    

arr = []
arr.clear()
arr = [1] + [0] * (4)
base = 0
while base < 100000:
    Increment(arr)
    base = ConvertToNum(arr)
    break

Scan([56123], 0, 0)        