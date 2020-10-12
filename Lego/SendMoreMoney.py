from math import factorial

digits = ['s','e','n','d','m','o','r','y']

def Add(top, btm):
    result = [0] * 5
    r = 0
    i = len(top) - 1
    while i >= 0:
        res = top[i] + btm[i] + r
        result[i + 1] = res % 10
        r = res // 10
        i -= 1
    result[0] = r
    return result

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
    global digits
    c = 0
    for i in range(factorial(len(arr))):
        c += 1
        #if c == 1000000:
        #    print(arr)
        #    return
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

        d = {}
        for i in range(len(digits)):
            d[digits[i]] = arr[i]
        t = [d['s'], d['e'], d['n'], d['d']]
        b = [d['m'], d['o'], d['r'], d['e']]
        r = Add(t, b)
        if r[0] == d['m'] and r[4] == d['y']:
            print("{} {} {}".format(t, b, r))
            return
        
        
    
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
GetLexi(array)
    
    
