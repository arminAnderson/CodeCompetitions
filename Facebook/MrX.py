def Study(s):
    

cases = int(input())
for i in range(cases):
    sequence = input()
    if len(sequence) == 1:
        try: 
            int(sequence)
            print("Case #{}: {}".format(i + 1, "0"))
        except ValueError:
            print("Case #{}: {}".format(i + 1, "1"))
    else:
        Study(sequence)
    