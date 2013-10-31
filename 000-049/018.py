lst = []
for line in open('018.txt', 'rt').xreadlines(): lst = [max(x+y[0], x+y[1]) for (x, y) in map(None, map(int,line.split(' ')), map(None, [0]+lst, lst+[0]))]
print max(lst)
