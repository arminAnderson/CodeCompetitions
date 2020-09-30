import math

def GetDigitCount(num):
    return int(math.log10(num))+1

panSet = set()    
def IsPandigital(arr):
    panSet.clear()
    panSet.add('0')
    for t in arr:
        if t in panSet:
            return False
        else:
            panSet.add(t)
    return len(panSet) == 10

temp = ""
for i in range(1, 10000):
    temp = ""
    j = 0
    for j in range(1, 10//GetDigitCount(i) + 1):
        jMax = j
        temp += str(i * j)
        if len(temp) >= 9:
            break
    if j > 1:
        if len(temp) == 9 and IsPandigital(temp):
            print("{} {} {}".format(temp, jMax, i))


