def c(x):
	s = 0
	while x > 0:
		s += (x % 10)**5
		x /= 10
	return s

print sum([x for x in xrange(2, 1000000) if c(x) == x])
