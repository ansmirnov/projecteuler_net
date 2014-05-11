__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

import math

def sum_fact(x):
    s = 0
    while x > 0:
        d = x % 10
        x /= 10
        s += math.factorial(d)
    return s

s = 0
for x in xrange(3, 100000):
    if x == sum_fact(x):
        s += x
print s