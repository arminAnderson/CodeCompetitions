num = int(input())
i = 0
smallest = 1

while False:
    i = 11
    if smallest % 2 == 0:
        while(i < num + 1):
            if smallest % i != 0:
                break
            i += 1
        if i == num + 1:
            print(smallest)
            exit()
    smallest += 1
