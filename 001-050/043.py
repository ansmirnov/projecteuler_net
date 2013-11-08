import math

MX = 0



def gen_pandigital(d, s=0, sm=0):
    if s > 1000000000:
        nd = int(math.log10(s))
        sub = s % 1000
        for a, b in [(3, 2), (4, 3), (5, 5), (6, 7), (7, 9), (8, 11), (9, 13), (10, 17)]:
            if not nd == a and s % b != 0:
                return
        print s
        global MX
        if len(d) == 0:
            print s
            return
    for x in d:
        if x == 0 and s == 0:
            continue
        gen_pandigital(d - set([x]), s*10 + x, sm+x)

#gen_pandigital(set(range(0, 9)))
#print MX

def gen_m(x):
    res = []
    i = 1
    while i * x < 1000:
        r = i*x
        if r > 99:
            if len(set(str(r))) == 3:
                res.append((r, r / 10))
        i += 1
    return res

print [len(gen_m(x)) for x in [2, 3, 5, 7, 11, 13, 17]]