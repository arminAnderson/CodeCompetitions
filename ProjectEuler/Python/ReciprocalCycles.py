def LongDiv(divisor):
    dividend = [1]
    divIndex = 0
    answer = []

    i = 0
    div = dividend[divIndex]
    pattern = False
    divs = []
    while div != 0 and not pattern and i < 1000:
        while div < divisor:
            divIndex += 1
            if divIndex == len(dividend):
                dividend.append(0)
            div *= 10
            div += dividend[divIndex]
            if div in divs:
                pattern = True
                break
            if div//divisor == 0:
                answer.append(0)
        divs.append(div)
        if pattern:
            break
        answer.append(div//divisor)
        div = div % divisor
        i +=1 
        
    return (len(answer))

largest = 0
sol = 0
for i in range(2, 1000):
    #continue
    j = LongDiv(i)
    if largest < j:
        sol = i
        largest = j

print("SOLUTION")
print(sol)
