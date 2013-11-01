import math


def is_prime(x):
    if x == 2: return True
    for i in xrange(2, int(math.sqrt(x) + 2)):
        if x % i == 0:
            return False
    if x == 1: return False
    return True


primes = [x for x in xrange(2, 1000000) if is_prime(x)]
sprimes = set(primes)

res = 0
nres = 1
for i in xrange(len(primes)):
    s = primes[i]
    for j in xrange(i+1, len(primes)):
        s += primes[j]
        if s in sprimes:
            if nres < j-i:
                nres = j-i
                res = s

print res