
def fastpow(a, n):
	if n == 0: return 1
	if n % 2 == 0:
		return fastpow(a, n/2)**2
	else:
		return fastpow(a, n-1)*a

print sum(map(int, list(str(fastpow(2, 1000)))))
