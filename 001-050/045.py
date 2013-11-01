__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'


def T(n):
    return n*(n+1)/2

def P(n):
    return n*(3*n - 1)/2

def H(n):
    return n*(2*n - 1)

TT = set([T(n) for n in xrange(100000)])
PP = set([P(n) for n in xrange(100000)])
HH = set([H(n) for n in xrange(100000)])

print TT & PP & HH