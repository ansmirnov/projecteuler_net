__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

import common

primes = [x for x in xrange(-1000, 1000) if common.is_prime(abs(x))]

nmax = 0
for a in primes:
    for b in primes:
        n = 0
        while common.is_prime(n*n + a * n + b):
            n += 1
        if n > nmax:
            nmax = n
            sa = a
            sb = b
            print sa, sb

print sa*sb