# Works but gets really slow at 15+
def Next(w, h, size):
    if w == size or h == size:
        return 1
    else:
        return Next(w + 1, h, size) + Next(w, h + 1, size)
#print("Recursive: {}".format(Next(0, 0, boxes)))

boxes = 20
size = boxes + 1
grid = []

for i in range(size):
    if i == 0:
        grid.append([1 for i in range(size)])
    else:
        grid.append([0 for i in range(size)])
        grid[i][0] = 1

for i in range(1, size):
    for j in range(1, size):
        grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

for r in grid:
    print(r)


