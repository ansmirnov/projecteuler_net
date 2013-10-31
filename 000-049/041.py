import math

def is_prime(x):
	for i in xrange(2, int(math.sqrt(x)+2)):
		if x % i == 0:
			return False
	if x == 1: return False
	return True

MX = 0

def gen_pandigital(d, s=0, sm=0):
    global MX
    if len(d) == 0:
        if sm == 3 or sm == 6:
            return
#        print s
        if s > MX and is_prime(s):
            MX = s
        return
    if len(d) == 1 and (list(d)[0] % 2 == 0):
        return
    for x in d:
        gen_pandigital(d - set([x]), s*10 + x, sm+x)

gen_pandigital(set(range(1, 8)))
print MX