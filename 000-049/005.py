from math import sqrt

prime = [2, 3, 5, 7, 11, 13, 17, 19]
aprime = [1]
aprime.extend(prime)

def fact (x): 
	r = [1]
	i = 0
	while x > 1:
		if x % prime[i] == 0:
			r.append(prime[i])
			x /= prime[i]
		else: i += 1
	return r

def to_dict(lst):
	r = {}
	for x in aprime: r[x] = 0
	for x in lst: r[x] += 1
	return r

def amax(d1, d2):
	r = {}
	for x in d1.keys():
		r[x] = max(d1[x], d2[x])
	return r

r = to_dict(fact(1))
for x in xrange(2, 21):
	r = amax(r, to_dict(fact(x)))

p = 1
for (x, y) in r.items(): 
    if x*y != 0: 
	    p *= x**y
print p
