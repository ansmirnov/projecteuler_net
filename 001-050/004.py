def ispal(x):
	s = str(x)
	return s == s[::-1]

R = 0

for x in xrange(1000):
	for y in xrange(1000):
		r = x*y
		if ispal(r): R = max(r, R)

print R