lst = range(2, 150000)
prime = []
while len(prime) < 10001:
	prime.append(lst[0])
	lst = [x for x in lst if x % prime[-1] != 0]
print prime[-1]