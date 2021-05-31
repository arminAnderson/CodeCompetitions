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
    c = 0
    for i in range(factorial(len(arr))):
        c += 1
        if c == 1000000:
            print(arr)
            return
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
    
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
GetLexi(array)