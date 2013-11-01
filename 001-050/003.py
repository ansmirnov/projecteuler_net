from math import sqrt

T = 600851475143
for x in xrange(1, int(sqrt(T)+2)): 
	if T % x == 0: 
		f = True
		for j in xrange(2, int(sqrt(x)+2)):
			if x % j == 0:
				f = False
				break
		if f: r = x

print r
