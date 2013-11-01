__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from common import is_prime, PRIMES

for x in xrange(2, 1000): is_prime(x)
primes = sorted(list(PRIMES))

def factor_prime(x):
    if is_prime(x):
        return set([x])
    res = set()
    for i in primes:
        if x == 1: return res
        while x % i == 0:
            res.add(i)
            x /= i
    res.add(x)
    return res

tmp = []
for x in xrange(2, 150000):
    lf = len(factor_prime(x))
    tmp.append(lf)
    ltmp = len(tmp)
    if tmp[len(tmp)-4:] == [4, 4, 4, 4]:
        print x-3, len(factor_prime(x))