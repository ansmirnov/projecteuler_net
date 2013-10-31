def gen():
    r = [(3, 3), (7, 7), (9, 9)]
#    for i in r:
 #       yield i[0]
    for i in r:
        for j in [1, 3, ]


"""/*import math


def is_prime(x):
    for i in xrange(2, int(math.sqrt(x) + 2)):
        if x % i == 0:
            return False
    if x == 1: return False
    return True


def fltr(x):
    s = 0
    if x % 10 == 1: return False
    while x != 0:
        d = x % 10
        if d % 2 == 0 or d == 5:
            return False
        s += d
        x /= 10
    return d != 1 and s % 3 != 0


def subset(x):
    dx = x
    s = set()
    while x != 0:
        s.add(x)
        x /= 10
    x = dx
    while x != 0:
        x %= 10**int(math.log10(x))
        s.add(x)
    return s

i = 11
t = 0
s = 0
while True:
    i += 2
    if i % 5
    if fltr(i):
        st = subset(i)
        f = True
        for j in st:
            if not is_prime(j):
                f = False
                break
        if not f: continue
        s += i
        print i
        t += 1
        if t == 11:
            break

print s

"""

