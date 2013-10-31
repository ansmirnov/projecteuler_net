from math import *

x, i = 0, 1
while True:
	x, i = x+i, i+1
	d = set()
	for j in xrange(1, int(sqrt(x)+2)):
		if x % j == 0:
			d.add(j)
			d.add(x/j)
	if len(d) >= 500:
		print x
		break