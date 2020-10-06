f = open("inputFiles/XorDecrypt.txt", "r")
nums = f.read().strip().split(',')
sequence = [int(c) for c in nums]

def Final(arr, key):
    ret = 0
    r = ''
    for i in range(0, len(arr)):
        letter = (chr(arr[i]^int(key[i%len(key)])))
        r += letter
        ret += ord(letter)

    print(r)
    print(ret)

def f(arr, key):
    s = ''
    a = ''
    b = ''
    c = ''
    d = ''
    for i in range(0, len(arr)):
        s = a
        a = b
        b = c
        c = d
        d = chr(arr[i]^int(key[i%len(key)]))
        if (a+b+c == "and" or a+b+c =="the") and (d == ' ' and s == ' '):
            return True
    return False

while(True):
    for a in range(26):
        for b in range(26):
            for c in range(26):
                if f(sequence, [a + 97, b + 97, c + 97]):
                    print("{} {} {}".format(chr(a + 97), chr(b + 97), chr(c + 97)))
                    Final(sequence, [a + 97, b + 97, c + 97])
                    exit()

