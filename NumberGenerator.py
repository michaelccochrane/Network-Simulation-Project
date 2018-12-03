import random
import matplotlib.pyplot as plt
import numpy as np

x = np.array([round(random.random(), 3) for _ in range(1000)])  # create array with 1000 random values between 0 and 1
plt.hist(x)     # plot array to historgram
plt.show()

x.sort()    # sorts array from lowest to highest, needed for kolmogorov smirnov

# KOLMOGOROV-SMIRNOV

dplus = np.empty(1000)  # create empty arrays for calculations of dplus and dminus
for i in range(1000):
    dplus[i] = (i + 1) / 1000.0- x[i]


dminus = np.empty(1000)
for j in range(1000):
    dminus[j] = x[j] - ((j + 1) - 1) / 1000.0

if np.max(dplus) < np.max(dminus):  # compare max values and assign highest to dmax
    dmax = np.max(dminus)
else:
    dmax = np.max(dplus)

dalpha = 0.043  # for N = 1000 and alpha = 0.05 from table A.8

print "Result of Kolmogorov-Smirnov Test: "
if dmax <= dalpha:      # test for uniformity by comparing dmax and dalpha
    print "dmax: ", dmax, " is less than or equal to dalpha: ", dalpha
    print "numbers are uniformly distributed"
else:
    print "dmax: ", dmax, " is greater than dalpha: ", dalpha
    print "numbers are not uniformly distributed"

# CHI-SQUARE

bin1 = []
bin2 = []
bin3 = []
bin4 = []
bin5 = []
bin6 = []
bin7 = []
bin8 = []
bin9 = []
bin10 = []

for p in range(1000):
    if 0.000 <= x[p] < 0.100:
        bin1.append(x[p])
    elif 0.1 <= x[p] < 0.2:
        bin2.append(x[p])
    elif 0.2 <= x[p] < 0.3:
        bin3.append(x[p])
    elif 0.3 <= x[p] < 0.4:
        bin4.append(x[p])
    elif 0.4 <= x[p] < 0.5:
        bin5.append(x[p])
    elif 0.5 <= x[p] < 0.6:
        bin6.append(x[p])
    elif 0.6 <= x[p] < 0.7:
        bin7.append(x[p])
    elif 0.7 <= x[p] < 0.8:
        bin8.append(x[p])
    elif 0.8 <= x[p] < 0.9:
        bin9.append(x[p])
    elif 0.9 <= x[p] <= 1:
        bin10.append(x[p])

xnotsquare = (((len(bin1) - 100)**2)/100) + (((len(bin2) - 100)**2)/100) + (((len(bin3) - 100)**2)/100) + (((len(bin4) - 100)**2)/100) + (((len(bin5) - 100)**2)/100) + (((len(bin6) - 100)**2)/100) + (((len(bin7) - 100)**2)/100) + (((len(bin8) - 100)**2)/100) + (((len(bin9) - 100)**2)/100) + (((len(bin10) - 100)**2)/100)
xalpha = 1022.816   # for n-1 = 999 and alpha = 0.05

print "Result of Chi-Square Test: "
if xnotsquare <= xalpha:      # test for uniformity by comparing xnotsquare and xalpha
    print "xnotsquare: ", xnotsquare, " is less than or equal to xalpha: ", xalpha
    print "numbers are uniformly distributed"
else:
    print "xnotsquare: ", xnotsquare, " is greater than xalpha: ", xalpha
    print "numbers are not uniformly distributed"

# TODO Steps 2 and 3