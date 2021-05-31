pents = set()
hex = set()

for i in range(1,1000000):
    pents.add( int(i*(3*i-1)/2) )
    hex.add( int(i*(2*i-1)) )

for i in range(286, 1000000):
    tri = i * (i + 1)/2
    if tri in hex and tri in pents:
        print(int(tri))
        exit()