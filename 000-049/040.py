def gen():
    s = 0
    while True:
        for x in str(s):
            yield x
        s += 1

x = gen()
t = 1
p = 1
for i in xrange(1000001):
    s = x.next()
    if i == t:
        p *= int(s)
        t *= 10
print p