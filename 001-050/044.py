__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

P = set([n*(3*n - 1)/2 for n in xrange(1, 10000)])

for i in P:
    for j in P:
        if i + j in P and abs(i - j) in P:
            print abs(i - j)