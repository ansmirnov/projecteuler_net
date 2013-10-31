from itertools import permutations
from math import log10

def gen_lst(lst):
	for i in xrange(1, len(lst)-1): 
		for x in permutations(lst, i): yield x

def to_int(x):
	r = 0
	for i in x:
		r *= 10
		r += i
	return r

lst = set(range(1, 10))

r = set()

for x in gen_lst(lst):
	lst2 = lst - set(x)
	for y in gen_lst(lst2):
		lst3 = lst2 - set(y)
		if len(lst3) < len(x) + int(log10(len(y))): continue
		if len(lst3) == 0: continue
		p = to_int(x)*to_int(y)
		if sorted(list(lst3)) == sorted(map(int, list(str(p)))): r.add(to_int(x)*to_int(y))
			#print x,y,to_int(x)*to_int(y)
print  r, sum(r)