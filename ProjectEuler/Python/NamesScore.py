def AlphabeticalOrder(first, second):
    a = 0
    b = 0
    index = 0
    while a == b:
        if index == len(first):
            return True
        if index == len(second):
            return False
        a = ord(first[index]) - 65
        b = ord(second[index]) - 65
        index += 1
    if a < b:
        return True
    return False

def ToHeap(arr):
    pMax = (len(arr) - 1) // 2
    i = pMax
    while(i > 0):
        CheckDown(i, arr, pMax, len(arr))
        i -= 1
    return arr

def CheckDown(index, arr, pMax, maxRef):
    if index > pMax:
        return
    child = index * 2
    if index * 2 + 1 < maxRef and AlphabeticalOrder(arr[child], arr[child + 1]):
        child += 1
    if AlphabeticalOrder(arr[index], arr[child]):
        temp = arr[index]
        arr[index] = arr[child]
        arr[child] = temp
        CheckDown(child, arr, pMax, maxRef)

def Sort(arr, length):
    while length > 1:
        temp = arr[length]
        arr[length] = arr[1]
        arr[1] = temp
        length -= 1
        CheckDown(1, arr, length // 2, length + 1)
        
    return arr
        
f = open("inputFiles/NamesScore.txt", "r")
names = f.readline().replace('"', "").split(",")
names.insert(0,"base")
#print(names)
ToHeap(names)
names = Sort(names, len(names) - 1)

sum = 0
for i in range(len(names)):
    charVal = 0
    for j in range(len(names[i])):
        charVal += ord(names[i][j]) - 64
    print(names[i] + ": " + str(charVal * (i)))
    sum += charVal * (i)

print(sum)
    