import math

def z_function (s):
	zr = [0]
	l, r = 0, 0
	n = len(s)
	for i in xrange(1, n):
		z = 0
		if i <= r: z = min(r-i+1, zr[i-l])
		while i+z < n and s[z] == s[i+z]: z += 1
		if i + z - 1 > r:
			l = i
			r = i + z - 1
		zr.append(z)
	return zr

def c(x):
	s = 1.
	r = ''
	st = []
	while True:
		if s in st:
			if len(st) - st.index(s) == 982: print x, r, len(st) - st.index(s)
			return len(st) - st.index(s)
			break
		st.append(s)
		if s == 0: return 0
		s *= 10
		c = int(math.floor(s / x))
		r = str(r) + str(c)
		s -= c*x
	return None

print max ([c(x) for x in xrange(1, 1000)])
