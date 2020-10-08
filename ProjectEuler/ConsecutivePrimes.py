def IsPrime(num):
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

primes = [2]
for i in range(3, 1000000, 2):
    if IsPrime(i):
        primes.append(i)

csum = [0] * (len(primes) + 1)
for i in range(0, len(primes)):
    csum[i + 1] = csum[i] + primes[i]

print("GENERATED PRIMES")
answer = 0
most = 1

i = len(primes) - 1
while i >= 0:
    s = 0
    e = most + 1
    while primes[i] > csum[e] - csum[s]:
        e+=1
        while primes[i] < csum[e] - csum[s] and e - s > most:
            s += 1
    if primes[i] == csum[e] - csum[s]:
        if e - s > most:
            answer = primes[i]
            most = e - s
    i -= 1
    
print("{} {}".format(answer, most))