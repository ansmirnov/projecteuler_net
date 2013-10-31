R, A = ['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]
CV = [[], [1], [1, 1], [1, 1, 5], [1, 5], [5], [5, 1], [5, 1, 1], [1, 1, 10], [1, 10]]


def ra(c):
    return A[R.index(c)]


def ar(c):
    return R[A.index(c)]


def roman_to_int(s):
    def r(lst):
        if lst == []: return 0
        m = lst.index(max(lst))
        return lst[m] - r(lst[:m]) + r(lst[m+1:])
    return r([ra(i) for i in s])

def int_to_roman(x):
    def list_to_str(lst):
        return ''.join(map(ar, lst))
    def mp(x, k):
        return [i*k for i in x]
    s = ''
    while x > 1000:
        x -= 1000
        s += 'M'
    return s + list_to_str(mp(CV[x / 100], 100)) + list_to_str(mp(CV[(x / 10) % 10], 10)) + list_to_str(mp(CV[x % 10], 1))

for str in open('roman.txt', 'rt').xreadlines():
    #print roman_to_int(str.strip())
    if roman_to_int(str.strip()) == 4956:
        print str.strip(), roman_to_int(str.strip()), int_to_roman(roman_to_int(str.strip())), len(str.strip()) - len(int_to_roman(roman_to_int(str.strip())))
#print sum([len(str.strip()) - len(int_to_roman(roman_to_int(str.strip()))) for str in open('roman.txt', 'rt').xreadlines()])

print int_to_roman(4956)