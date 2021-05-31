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
        
def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

c = 10
for i in range(10):

    array = list(range(1, c))
    c -= 1
    possible = []
    possible.append(tuple(array))
    GetLexi(array)
    possible.reverse()

    for perm in possible:
        num = 0
        for p in perm:
            num *= 10
            num += p
        if IsPrime(num):
            print(num)
            exit()