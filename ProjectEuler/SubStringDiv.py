from math import factorial

def ReverseSectionOfArr(arr, start):
    swapAmount = (len(arr) - start)//2
    k = len(arr) - 1
    for i in range(swapAmount):
        i += start
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
        k -= 1
    return arr

def GetLexi(arr):
    for i in range(factorial(len(arr))):
        i = len(arr) - 1
        k = len(arr) - 2
        while(arr[k] > arr[k+1]):
            k -= 1
            if(k == -1):
                print("FINISHED")
                return
        while arr[i] < arr[k]:
            i -= 1
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
        arr = ReverseSectionOfArr(arr, k + 1)
        possible.append(tuple(arr))

possible = []
array = [0,1,2,3,4,5,6,7,8,9]
div = [2,3,5,7,11,13,17]
possible.append(tuple(array))
GetLexi(array)

result = 0

for perm in possible:
    index = 1
    e = False
    for d in div:
        num = 0
        for i in range(3):
            num *= 10
            num += perm[index + i]
        if num % d != 0:
            e = True
            break
        index += 1
    if not e:
        num = 0
        for i in perm:
            num *= 10
            num += i
        result += num

print(result)
