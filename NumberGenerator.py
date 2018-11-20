import random
import matplotlib.pyplot as plt
import numpy as np

x = np.array([round(random.random(), 3) for _ in range(1000)])
plt.hist(x)
plt.show()

x.sort()    #sorts array from lowest to highest, needed for kolmogorov smirnov
print x


dplus = np.empty(1000)
for i in range(1000):
    dplus[i] = (i + 1) / 1000.0- x[i]


dminus = np.empty(1000)
for j in range(1000):
    dminus[j] = x[j] - ((j + 1) - 1) / 1000.0

print dplus
print dminus
print np.amax(dplus)
print np.amax(dminus)

if np.max(dplus) < np.max(dminus):
    dmax = np.max(dminus)
else:
    dmax = np.max(dplus)

print dmax
#TODO compare dmax with da