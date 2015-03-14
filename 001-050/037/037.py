import math

PRIME = set()

def is_prime(x):
    if x in PRIME:
        return True
    for i in xrange(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    if x <= 1: return False
    PRIME.add(x)
    return True


def is_prime_all(x):
    if x < 10:
        return False
    l = int(math.ceil(math.log10(x)))
    for i in xrange(1, l+1):
        if not is_prime(x / 10**(l-i)):
            return False
        if not is_prime(x % 10**i):
            return False
    return True


s = 0

def f(cur, append=(1, 3, 7, 9)):
    global s
    if not is_prime(cur):
        return
    if is_prime_all(cur):
        s += cur
    for x in append:
        f(cur * 10 + x)

f(2)
f(3)
f(5)
f(7)
print s