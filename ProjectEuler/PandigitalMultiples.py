panSet = set()

def IsPandigital(arr):
    panSet.clear()
    panSet.add(0)
    for t in arr:
        if t in panSet:
            return False
        else:
            panSet.add(t)
    return len(panSet) == 10

longest = 0

for i in range(1, 10000000):
    arr = []
    for j in range(1, 10):
        temp = []
        num = i * j
        while num > 0:
            temp.append(num % 10)
            num //= 10
        k = len(temp) - 1
        while k != -1 and len(arr) < 9:
            arr.append(temp[k])
            k -= 1
        if len(arr) == 9:
            break
    if IsPandigital(arr):
        l = 0
        for v in arr:
            l *= 10
            l += v
        longest = max(longest, l)

print(longest)