d = dict(map(lambda x: (str(x), set()), range(10)))
for s in open('keylog.txt', 'rt').xreadlines():
	a, b, c = s.strip()
	d[b].add(a)
	d[c].add(b)

s = ''

f = False
while d != {}:
	for i in d.keys():
		if len(d[i]) == 0:
			ff = False
			for j in d.keys():
				if i in d[j]:
					d[j].discard(i)
					ff = True
			del d[i]
			if f or ff: s = s + i
	f = True

print s
