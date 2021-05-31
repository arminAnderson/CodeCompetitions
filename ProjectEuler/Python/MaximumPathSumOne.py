def Step(r, c, v):
    if r == len(pyr):
        return v
    if c == len(pyr[r]):
        return -1
    v += pyr[r][c]
    return max(Step(r + 1, c, v), Step(r + 1, c + 1, v))
    
pyr = []
f = open("inputFiles/MaximumPathSumOne.txt", "r")
for line in f.readlines():
    pyr.append([int(i) for i in line.split()])

print(Step(0,0,0))