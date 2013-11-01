m = 0
for i in xrange(1, 10000):
    r = set()
    s = ''
    for j in xrange(1, 10):
        t = i * j
        ret = False
        tt = t
        while t > 0:
            d = t % 10
            if d in r:
                ret = True
                break
            r.add(d)
            t /= 10
        if ret: break
        s = s + str(tt)
    if s == '' or s.count('0') != 0: continue
    if len(s) < 10:
        if m < int(s):
            m = int(s)
print m
