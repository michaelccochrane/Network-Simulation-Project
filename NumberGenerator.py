import random
import matplotlib.pyplot as plt
import numpy as np

x = np.array([round(random.random(), 3) for _ in range(1000)])  #create array with 1000 random values between 0 and 1
plt.hist(x)     #plot array to historgram
plt.show()

x.sort()    #sorts array from lowest to highest, needed for kolmogorov smirnov
print x


dplus = np.empty(1000)  #create empty arrays for calculations of dplus and dminus
for i in range(1000):
    dplus[i] = (i + 1) / 1000.0- x[i]


dminus = np.empty(1000)
for j in range(1000):
    dminus[j] = x[j] - ((j + 1) - 1) / 1000.0

print dplus
print dminus
print np.amax(dplus)    #find max value in dplus and dminus
print np.amax(dminus)

if np.max(dplus) < np.max(dminus):  #compare max values and assign highest to dmax
    dmax = np.max(dminus)
else:
    dmax = np.max(dplus)

print dmax
#TODO KOLMOGOROV: compare dmax with da, draw conclusion
#TODO CHI-SQUARE: everything