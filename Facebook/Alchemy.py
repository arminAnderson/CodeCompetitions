cases = int(input())
for i in range(cases):
    length = int(input())
    sequence = input()
    ret = "N"
    if abs(sequence.count("A") - sequence.count("B")) == 1:
        ret = "Y"
    print("Case #{}: {}".format(i + 1, ret))
    