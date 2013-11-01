from fractions import Fraction

N = 100 - 1
lst = [2] + reduce(lambda x, y: x+y, [[1, 2*i, 1] for i in xrange(1, 100)])
rlst = lst[:N][::-1]
r = lst[N]
for x in rlst:
	r = Fraction(1, r) + x

s = 0
x = r.numerator
while x > 0:
	s += x % 10
	x /= 10
print s