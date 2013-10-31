D = {}
def d(x):
	if x in D.keys(): return D[x]
	D[x] = sum([i for i in xrange(1, int(x/2+2)) if x % i == 0])
	return D[x]

print sum([x for x in xrange(1, 10001) if d(d(x)) == x and x != d(x)])
