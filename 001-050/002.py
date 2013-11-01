px = 1
x = 2
s = 0
while True:
	if x >= 4000000: break
	if x % 2 == 0: s += x
	x, px = x+px, x
print s