sum = 2
v = 0
for one in range(0, 200):
    for two in range(0, 101):
        v = one + two * 2
        if v > 200:
            break
        if v == 200:
            sum += 1
            break
        for five in range(0, 41):
            v = one + two * 2 + five * 5
            if v > 200:
                break
            if v == 200:
                sum += 1
                break
            for ten in range(0, 21):
                v = one + two * 2 + five * 5 + ten * 10
                if v > 200:
                    break
                if v == 200:
                    sum += 1
                    break
                for twenty in range(0, 11):
                    v = one + two * 2 + five * 5 + ten * 10 + twenty * 20
                    if v > 200:
                        break
                    if v == 200:
                        sum += 1
                        break
                    for fifty in range(0, 5):
                        v = one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50
                        if v > 200:
                            break
                        if v == 200:
                            sum += 1
                            break
                        for hundred in range(0, 3):
                            v = one + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred * 100
                            if v > 200:
                                break
                            if v == 200:
                                sum += 1
                                break
    
print(sum)
