inArr = [(2,4), (5,9), (7,10)]
lines = []
i = 1
line = [inArr[0][0], -1]
while i < len(inArr):
    while i < len(inArr) and inArr[i - 1][1] >= inArr[i][0]:
        line[1] = inArr[i][1]
        i += 1
    line[1] = inArr[i - 1][1]
    lines.append(line[:])
    if i < len(inArr):
        line[0] = inArr[i][0]
    i += 1

print(lines)
         