r = {}

def f(i, j):
	if i == 0 or j == 0: return 1
	if (i, j) not in r.keys(): r[(i, j)] = f(i-1, j) + f(i, j-1)
	return r[(i, j)]

print f(20, 20)
