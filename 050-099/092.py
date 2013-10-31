from itertools import *
import math

def dset(x):
	def dlist(x):
		while x > 0:
			yield x % 10
			x /= 10
	return tuple(sorted(list(dlist(x))))

def nums(n):
	def dnums(n, st):
		if n == 0: return [[]]
		return reduce(lambda x,y: x+y, [map(lambda x: [i] + x, dnums(n-1, i)) for i in xrange(st, 10)])
	return map(tuple, dnums(n, 0))
def anums(n): return filter(lambda x: sum(x) != 0, reduce(lambda x,y: x+y, [nums(i) for i in xrange(1, n+1)]))

def turn(x): return dset(sum([i**2 for i in x]))

C = {(1,): (1,), (8, 9,): (8,9,)}
def c(x):
	if x in C.keys(): return C[x]
	r = x
	rr = [x]
	while r not in C.keys():
		r = turn(r)
		rr.append(r)
	for i in rr: C[i] = C[r]
	return C[x]

def cr(x):
	def nper(n, d):
		return math.factorial(n) / reduce (lambda x, y: x*y, [math.factorial(x) for x in d.values()])
	d = {}
	for i in x:
		if i in d.keys():
			d[i] += 1
		else:
			d[i] = 1
	n = len(x)
	if 0 in d.keys():
		r = nper(n, d)
		d[0] -= 1
		return r - nper(n-1, d)
	else:
		return nper(n, d)

print sum([cr(x) for x in (anums(3)) if c(x) == (8, 9)])
