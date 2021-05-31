f = open("inputFiles/LargestProductInGrid.txt", "r")

arr = [] 
size = 20
adj = 4
largest = 0

for line in f.readlines():
    temp = []
    for c in map(int, line.split()):
        try:
            temp.append(int(c))
        except ValueError:
            continue
    arr.append(temp)

temp = 1
#horizontal
for i in range(size):
    for j in range(size - adj + 1):
        for k in range(adj):
            temp *= arr[i][j + k]
        largest = max(largest, temp)
        temp = 1 
#vertical
for i in range(size):
    for j in range(size - adj + 1):
        for k in range(adj):
            temp *= arr[j + k][i]
        largest = max(largest, temp)
        temp = 1 

#d-right
for i in range(size - adj + 1):
    for j in range(size - adj + 1):
        for k in range(adj):
            temp *= arr[i + k][j + k]
        largest = max(largest, temp)
        temp = 1 

#d-left
for i in range(size - adj + 1):
    for j in range(size - adj + 1):
        for k in range(adj):
            temp *= arr[i + k][size - (j + k) - 1]
        largest = max(largest, temp)
        temp = 1 

print(largest)

