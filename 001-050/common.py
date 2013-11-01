__author__  = 'Andrey Smirnov'
__email__   = 'mail@ansmirnov.ru'

import math

PRIMES = set()

def is_prime(x):
    if x in PRIMES:
        return True
    if x == 2: return True
    for i in xrange(2, int(math.sqrt(x) + 2)):
        if x % i == 0:
            return False
    if x == 1: return False
    PRIMES.add(x)
    return True

