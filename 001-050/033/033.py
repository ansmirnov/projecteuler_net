__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'


def gcd(a, b):
    return gcd(b, a % b) if b else a

num,  denom = 1, 1

for a in xrange(1, 10):
    for b in xrange(0, 10):
        for c in xrange(1, 10):
            for d in xrange(0, 10):
                if b == 0 or d == 0:
                    continue
                if a == c:
                    continue
                elif a == d:
                    tx, ty = b, c
                elif b == c:
                    tx, ty = a, d
                elif b == d:
                    tx, ty = a, c
                else:
                    continue
                x = a * 10 + b
                y = c * 10 + d
                if x > y:
                    continue
                if ty and (tx+.0) / (ty + .0) == (x + .0) / (y + .0):
                    print x, y, tx, ty, tx / ty
                    num *= x
                    denom *= y

g = gcd(num, denom)
print num/g, denom/g