f = open("inputFiles/LargestProductInSeries.txt", "r")

size = 13
largest = 0
arr = []

for line in f.readlines():
    for c in line:
        try:
            arr.append(int(c))
        except ValueError:
            continue

temp = 1
for i in range(len(arr)):
    for j in range(size):
        if arr[i + j] == 0:
            break
        else:
            temp *= arr[i + j]
    largest = max(largest, temp)
    temp = 1

print(largest)