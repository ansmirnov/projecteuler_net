x = 1
c = 4
d = 2
s = 0
while x <= 1001*1001:
	s += x
	x += d
	c -= 1
	if c == 0:
		c = 4
		d += 2
print s
