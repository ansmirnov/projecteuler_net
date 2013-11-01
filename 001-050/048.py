__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

from common import powmod

modulo = 10000000000
print sum([powmod(i, i, modulo) for i in xrange(1, 1001)]) % modulo
