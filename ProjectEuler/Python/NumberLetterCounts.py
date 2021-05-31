def GetLetters(i):
    if i < 20:
        return nums[i - 1]
    elif i < 100:
        temp = i
        temp -= 20
        temp //= 10
        rem = 0
        if i % 10 != 0:
            rem = nums[i % 10 - 1]
        return tens[temp] + rem
    else:
        temp = i
        temp //= 100
        rem = -3
        if i % 100 != 0:
            rem = GetLetters(i % 100)
        return nums[temp - 1] + hundred_and + rem

# 1 - 19
nums = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
# 20 - 90
tens = [6, 6, 5, 5, 5, 7, 6, 6]
hundred_and = 10

sum = 0
for i in range(1, 1000):
    #print("{}, {}".format(i, GetLetters(i)))
    sum += GetLetters(i)

print(sum + 11)


