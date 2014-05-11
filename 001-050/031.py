__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

SET = [1, 2, 5, 10, 20, 50, 100, 200]
_RES = [
    set([()]),
    set([(1, )]),
]

def RES(x):
    if x < 0:
        return set()
    return _RES[x]

for x in xrange(2, 201):
    _RES.append(set(reduce(lambda x, y: x + y, [map(lambda l: tuple(sorted(l + (c,))), RES(x-c)) for c in SET  if c <= x])))
    print x

print len(_RES[200])
