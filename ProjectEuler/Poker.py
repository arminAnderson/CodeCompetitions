# C -> D -> H -> S
def BuildHands(hand, arr):
    for card in hand:
        val = card[:1]
        try:
            val = int(val)
        except:
            if val == "T":
                val = 10
            elif val == "J":
                val = 11
            elif val == "Q":
                val = 12
            elif val == "K":
                val = 13
            else:
                val = 14

        arr[val - 2][0] += 1
        suit = 4
        if card[1:] == "C":
            suit = 1
        elif card[1:] == "D":
            suit = 2
        elif card[1:] == "H":
            suit = 3
        arr[val - 2][suit] = 1

def GetScore(arr):
    f= set()
    cards = set()

    flush = False
    strt = True
    royal = False

    foundCard = False
    largestCard = -1
    largestGroup = 0
    groups = []
    

    i = len(arr) - 1
    while i >= 0:
        if arr[i][0] > 0:
            cards.add(i)
            if largestCard == -1:
                largestCard = i
            g = 0
            for s in range(1, 5):
                if arr[i][s] == 1:
                    f.add(s)
                    g += 1
            largestGroup = max(largestGroup, g)
            if g > 1:
                groups.append(i)
        i -= 1
    
    for i in range(1, 5):
        if arr[largestCard - i][0] == 0:
            strt = False
            break
    
    flush = len(f) == 1
    royal = flush and strt and largestCard == 12
    
    #print()
    #print("STATS| biggest: {}, flush? {}, straight? {}, royal? {}".format(largestCard, flush, strt, royal))
    #print("STATS| largest group: {}, groups {}".format(largestGroup, groups))

    if royal:
        #print("ROYAL")
        return [108]
    elif flush and strt:
        #print("S FLUSH")
        return [107,largestCard]
    elif largestGroup == 4:
        #print("FOUR")
        return [106, arr]
    elif len(groups) == 2 and largestGroup == 3:
        #print("HOUSE")
        return [105, groups]
    elif flush:
        #print("FLUSH")
        return [104, largestCard]
    elif strt:
        #print("STRAIGHT")
        return [103, largestCard]
    elif largestGroup == 3:
        #print("THREE")
        return [102, arr]
    elif len(groups) == 2 and largestGroup == 2:
        #print("TWO PAIR")
        return [101, arr]
    elif largestGroup == 2:
        #print("PAIR")
        return [100, arr]
    else:
        #print(largestCard + 2)
        return [largestCard]
    

f = open("inputFiles/Poker.txt", "r")

iters = 5
for line in f.readlines():
    handA = []
    handB = []
    for i in range(13):
        handA.append([0,0,0,0,0])
        handB.append([0,0,0,0,0])

    BuildHands(line[:14].split(" "), handA)
    BuildHands(line[15:].replace("\n", "").split(" "), handB)
    
    a = GetScore(handA)
    b = GetScore(handB)
    if a > b:
        print("A WINS")
    elif b > a:
        print("B WINS")
    else:
        #TODO THIS PART with return type
        print("TIE")

    #print("{} | {}".format(handA, line[:14].split(" ")))
    if iters == 0:
        break
    iters -= 1