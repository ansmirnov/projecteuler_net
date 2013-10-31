import math

N = 10000


def is_prime(x):
    if x == 2: return True
    for i in xrange(2, int(math.sqrt(x) + 2)):
        if x % i == 0:
            return False
    if x == 1: return False
    return True


primes = [i for i in xrange(2, N) if is_prime(i)]


def is_candy(x):
    return not (x in primes or x % 2 == 0)


for x in filter(is_candy, range(2, N)):
    r = 0
    i = 0
    while x > r:
        i += 1
        r = 2 * i**2
        f = True
        if x-r in primes:
            f = False
            break
    if f:
        print x
