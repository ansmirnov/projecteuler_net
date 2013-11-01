from numpy import *
DATA = matrix(loadtxt("011.txt"))
def data(i, j):
	try:
		return DATA[i, j]
	except:
		return 0
m = 0
for i in xrange(DATA.shape[0]):
	for j in xrange(DATA.shape[1]):
		m = max([
		    m,
		    data(i,j)*data(i+1,j+1)*data(i+2,j+2)*data(i+3,j+3),
		    data(i,j)*data(i-1,j+1)*data(i-2,j+2)*data(i-3,j+3),
		    data(i,j)*data(i,j+1)*data(i,j+2)*data(i,j+3),
		    data(i,j)*data(i+1,j)*data(i+2,j)*data(i+3,j),
		])
print int(m)
