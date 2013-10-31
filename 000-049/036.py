def ispal(s): return s == s[::-1]
print sum([x for x in xrange(1000001) if ispal(str(x)) and ispal(str(bin(x)[2:]))])
