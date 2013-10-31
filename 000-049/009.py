for a in xrange(1, 1001):
	for b in xrange(1, 1001-a):
		c = 1000 - a - b
		if a+b+c == 1000 and a**2 + b**2 == c**2:
			print a * b * c
