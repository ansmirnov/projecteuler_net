import math

MX = 0



def gen_pandigital(d, s=0, sm=0):
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

gen_pandigital(set(range(0, 9)))
print MX