cases = int(input())
for i in range(cases):
    length = int(input())
    arrA = input()  #can enter
    arrB = input()  #can leave
    ret = []
    for j in range(0, length):
        k = j
        charArr = []
        for pos in range(length):
            charArr.append("N")
        ret.append(charArr)

        while k < length:
            ret[len(ret) - 1][k] = "Y"
            if (k < length - 1 and arrA[k + 1] == "N") or arrB[k] == "N":
                break
            k += 1

        k = j
        while k > -1:
            ret[len(ret) - 1][k] = "Y"
            if (k > 0 and arrA[k - 1] == "N") or arrB[k] == "N":
                break
            k -= 1
    print("Case #{}:".format(i + 1))
    for elem in ret:
        for e in elem:
            print(e,end="")
        print()