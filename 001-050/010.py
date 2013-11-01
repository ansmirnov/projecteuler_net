from math import *

def isPrime (x):
	for j in xrange(2, int(sqrt(x)+2)):
		if x % j == 0 and x != j:
			return False
	return True

s = 0
for x in xrange(2, 2000000):
	 if isPrime(x): s += x
print s