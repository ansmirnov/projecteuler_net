
fib = [0, 1, 1]
i = 2
while True:
	i += 1
	f = fib[-1] + fib[-2]
	if f >= 10**999: break
	fib.append(f)
print i
