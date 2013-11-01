from math import sqrt
from copy import copy

def divisors (x):
	d = set()
	for j in xrange(1, int(sqrt(x)+2)):
		if x % j == 0:
			d.add(j)
			d.add(x/j)
	return d

MAX = 30000

ab = [i for i in xrange(12, MAX+1) if sum(divisors(i)) > 2*i]
ba = copy(ab)
ba.reverse()

r = set(range(1, MAX+1))

for x in ab:
	for y in ba:
		if x + y <= MAX: r.discard(x+y)

print sum(r)
