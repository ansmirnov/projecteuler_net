def n_p(p):
    r = set()
    for x in xrange(1, p+1):
        for y in xrange(1, p-x):
                z = p-x-y
                x2, y2, z2 = x**2, y**2, z**2
                if x2 + y2 == z2 or x2 + z2 == y2 or z2 + y2 == x2:
                    r.add(tuple(sorted((x,y,z))))
    return len(r)

m, nm = 0, 0
for p in xrange(1, 1001):
    r = n_p(p)
    print p, r
    if r > m:
        m = r
        nm = p
print nm