f = open("inputFiles/XorDecrypt.txt", "r")
nums = f.read().split(",")
key = 0
index = 0

key = "aaa"
print((key))
for n in nums:
    c = int(n) ^ key
    #print(chr(c))