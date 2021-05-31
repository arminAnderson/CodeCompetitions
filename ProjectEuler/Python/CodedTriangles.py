def GenerateTriNums():
    s = set()
    for i in range(1,1000001):
        s.add(int(.5 * i * (i + 1)))
    return s

tris = GenerateTriNums()
f = open("inputFiles/CodedTriangles.txt", "r")

result = 0
for word in f.readline().replace('"', '').split(","):
    value = 0
    for letter in word:
        value += ord(letter) - 64
    if value in tris:
        result += 1

print(result)
    

