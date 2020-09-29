def IsPrime(num):
    if num % 2 == 0 and num > 2:
        return 0
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

solution = 0

for i in range(2, 1000000):
    arr = []
    og = i
    while i > 0:
        arr.append(i % 10)
        i //= 10
    sol = True
    for c in range(len(arr)):
        temp = arr[0]
        f = temp
        for j in range(len(arr)-1):
            arr[j] = arr[j + 1]
            f *= 10
            f += arr[j]
        arr[len(arr)-1] = temp
        if not IsPrime(f):
            sol = False
            break
    if sol:
        solution += 1

print(solution)
