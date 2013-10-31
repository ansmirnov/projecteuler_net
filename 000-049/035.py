import math
from itertools import permutations

def is_prime(x):
	for i in xrange(2, int(math.sqrt(x)+2)):
		if x % i == 0:
			return False
	if x == 1: return False
	return True

def anext(x):
	return x / 10 + (x % 10) * 10**(int(math.log10(x)))

def is_circular(x):
	if x == 2 or x == 3 or x == 5: return True
	if x % 2 == 0 or x % 5 == 0: return False
	s = 0
	xx = x
	while x > 0:
		i = x % 10
		x /= 10
		if i % 2 == 0 or i == 5 or i == 0: return False
		s += i
	if s % 3 == 0: return False
	x = anext(xx)
	for i in xrange(int(math.log10(x)+1)):
		if not is_prime(x): return False
		x = anext(x)
	return True

print len((filter(is_circular, xrange(2, 1000000))))
