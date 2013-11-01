from itertools import *
import math

CNT = 7

def dset(x):
	def dlist(x):
		i = 0
		while x > 0 or i < CNT:
			yield x % 10
			x /= 10
			i += 1
	return tuple(sorted(list(dlist(x))))

def nums(n):
	def dnums(n, st):
		if n == 0: return [[]]
		return reduce(lambda x,y: x+y, [map(lambda x: [i] + x, dnums(n-1, i)) for i in xrange(st, 10)])
	return map(tuple, dnums(n, 0))
def anums(n): return filter(lambda x: sum(x) != 0, nums(CNT))

def turn(x): return dset(sum([i**2 for i in x]))

C = {dset(1): dset(1), dset(89): dset(89)}
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
	return nper(n, d)

#for x in (anums(CNT)):
#	if c(x) == dset(89):
#		print x, cr(x)

print sum([cr(x) for x in (anums(CNT)) if c(x) == dset(89)])
