from common import is_prime
from collections import Counter

def IntToCounter(x):
    res = Counter()
    while x != 0:
        res[x % 10] += 1
        x /= 10
    return res

primes = dict([(x, IntToCounter(x)) for x in xrange(1001, 10000) if is_prime(x)])

res = set()
for a in primes.items():
    for b in primes.items():
        if a[0] == b[0] or a[1] != b[1]: continue
        aa = min(a[0], b[0])
        bb = max(a[0], b[0])
        cc = bb + (bb - aa)
        if cc in primes.keys() and primes[cc] == a[1]:
            res.add((aa, bb, cc))

for x in res:
    print x, str(x[0])+str(x[1])+str(x[2])

