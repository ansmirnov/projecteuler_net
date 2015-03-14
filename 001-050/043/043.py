import math


def gen_m(x):
    res = []
    i = 1
    while i * x < 1000:
        r = i*x
        res.append(r)
        i += 1
    return res

Q = [gen_m(x) for x in [2, 3, 5, 7, 11, 13, 17]]

_ALL = set(range(10))
S = 0


def f(x):
    global S
    l = int(math.ceil(math.log10(x)))
    if l == 10:
        S += x
        return
    used = set()
    _x = x
    while _x:
        used.add(_x % 10)
        _x /= 10
    tail = x % 100
    for q in Q[l-3]:
        if q / 10 != tail or q % 10 in used:
            continue
        f(x*10 + q % 10)

for i in xrange(1000):
    if len(set(str(i))) == 3:
        f(i)

print S
