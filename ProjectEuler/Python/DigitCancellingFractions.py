def Reduce(i, j):
    div = i
    while div > 1 and i > 1:
        if i % div == 0 and j % div == 0:
            i //= div
            j //= div
        div -= 1
    return [i, j]

digit_i = [0,0]
digit_j = [0,0]
finals = []
for i in range(10, 100):
    for j in range(i + 1, 100):
        digit_i[0] = i % 10
        digit_i[1] = (i//10) % 10
        digit_j[0] = j % 10
        digit_j[1] = (j//10) % 10
        result = 0
        if not 0 in digit_j:
            if digit_i[0] == digit_j[1]:
                result = digit_i[1]/digit_j[0]
            elif digit_i[1] == digit_j[0]:
                result = digit_i[0]/digit_j[1]
            if result == i/j:
                finals.append(Reduce(i,j))
            
end = finals[0]
for i in range(1, len(finals)):
    end[0] *= finals[i][0]
    end[1] *= finals[i][1]

print(Reduce(end[0], end[1]))