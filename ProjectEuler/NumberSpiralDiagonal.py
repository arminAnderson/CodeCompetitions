sum = 1
sr = 3

dimension = 1001 // 2

for i in range(dimension):
    sr_t = sr * sr
    sum += (4 * sr_t) - (6 * sr - 6)
    sr += 2

print(sum)