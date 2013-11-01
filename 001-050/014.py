def collatz_sequence(x):
    r = 1
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1 
       r+=1
    return r

m = 0

for x in xrange(1000000):
	if x % 10000 == 0: print x
	m = max(m, collatz_sequence(x))