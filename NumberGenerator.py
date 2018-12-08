import matplotlib.pyplot as plt
import numpy as np
from math import log

print 'NET4001 Final Project by Michael Cochrane (100941655) and Joshua Nelson (100981092)'
x = np.random.uniform(0, 1, 1000)  # create array with 1000 random values between 0 and 1
plt.hist(x)     # plot array to historgram
plt.title('Uniform Distribution')
plt.show()

x.sort()    # sorts array from lowest to highest, needed for kolmogorov smirnov

# KOLMOGOROV-SMIRNOV

dplus = np.empty(1000)  # create empty arrays for calculations of dplus and dminus
for i in range(1000):
    dplus[i] = (i + 1) / 1000.0 - x[i]


dminus = np.empty(1000)
for h in range(1000):
    dminus[h] = x[h] - ((h + 1) - 1) / 1000.0

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

# INVERSE TRANSFORM

exprand = np.empty(1000)    # empty array to put exponentially distributed numbers into

for r in range(1000):
    exprand[r] = (-1.0/3.0)*log(x[r])

plt.hist(exprand)           # plot exponential distribution to histogram
plt.title('Exponential Distribution')
plt.show()

# Q-Q PLOT

y = np.empty(1000)
for j in range(1000):
    y[j] = ((j+1)-0.5)/1000
    y[j] = (-1.0/3.0)*log(y[j])

plt.scatter(exprand, y)
plt.title('Q-Q Plot')
plt.show()

# Single Server Simulation
mu = 10  # value of mu


class Stats:
    def __init__(self, avgw, avgl):
        self.w = avgw
        self.l = avgl

def server_simulation(lamb):

    interarrivaltime = np.empty(1000)  # array for inter-arrival times
    servicetime = np.empty(1000)  # array for service times

    interarrivaltime[0] = 0  # inter-arrival time for first packet will always be 0

    for inttime in range(999):  # loop for generating inter-arrival times using inverse transform
        interarrivaltime[inttime + 1] = (-1.0 / lamb) * log(x[inttime])

    for servtime in range(1000):  # loop for generating service times using inverse transform
        servicetime[servtime] = (-1.0 / mu) * log(x[servtime])

    arrivaltime = np.empty(1000)  # array for arrival times
    arrivaltime[0] = 0  # arrival time first packet will always be 0
    for a in range(999):  # arrival time for packet n = arrivaltime[n-1] + interarrivaltime[n]
        arrivaltime[a + 1] = arrivaltime[a] + interarrivaltime[a + 1]

    timeserviceends = np.empty(1000)  # array for the time when service ends
    timeserviceends[0] = servicetime[0]  # time service ends for the first packet will always be its service time
    for tse in range(999):  # loop for generating time service ends
        if arrivaltime[tse + 1] >= timeserviceends[tse]:  # if arrival time of n is greater than time service ends of n-1
            timeserviceends[tse + 1] = arrivaltime[tse + 1] + servicetime[tse + 1]  # packet will not be queued
        else:
            timeserviceends[tse + 1] = timeserviceends[tse] + servicetime[tse + 1]

    timeservicebegins = np.empty(1000)  # array for time service begins
    timeservicebegins[0] = 0  # for first packet service will always begin at 0
    for tsb in range(999):  # loop for generating time service begins
        if arrivaltime[tsb + 1] >= timeserviceends[tsb]:
            timeservicebegins[tsb + 1] = arrivaltime[tsb + 1]
        else:
            timeservicebegins[tsb + 1] = timeserviceends[tsb]

    waittime = np.empty(1000)
    for wt in range(1000):
        waittime[wt] = timeserviceends[wt] - arrivaltime[wt]

    totalwaittime = np.sum(waittime)  # total wait time will be the sum of all wait times
    totalsimulationtime = timeserviceends[999]  # total simulation time will be when the service of the last packets ends

    W = totalwaittime / 1000  # the average wait time will be total wait time divided by number of clients
    L = totalwaittime / totalsimulationtime  # average clients in system will be total wait time divided by total simulation time

    return Stats(W, L)


samplesize = 100

actualW = np.empty(samplesize)
actualL = np.empty(samplesize)

for inst in range(samplesize):
    actualW[inst] = server_simulation(inst+1).w
    actualL[inst] = server_simulation(inst+1).l

theoryL = np.empty(samplesize)
theoryW = np.empty(samplesize)

for c in range(samplesize):
    lam = c + 1.0
    if lam == mu:
        theoryL[c] = 0
        theoryW[c] = 0
    else:
        theoryL[c] = lam / (mu - lam)
        theoryW[c] = 1 / (mu - lam)


plt.scatter(range(0, samplesize), actualW, color='red', label='Simulated W')
plt.scatter(range(0, samplesize), theoryW, color='blue', label='Theoretical W')
plt.title('Simulated vs Theoretical Average Wait Time in System')
plt.xlabel('Arrival Rate')
plt.ylabel('Average Wait Time in System')
plt.legend()
plt.show()

plt.scatter(range(0, samplesize), actualL, color='red', label='Simulated L')
plt.scatter(range(0, samplesize), theoryL, color='blue', label='Theoretical L')
plt.title('Simulated vs Theoretical Average Clients in System')
plt.xlabel('Arrival Rate')
plt.ylabel('Average Clients in System')
plt.legend()
plt.show()

plt.scatter(range(0, samplesize), theoryL)
plt.title('Theoretical L')
plt.xlabel('Arrival Rate')
plt.ylabel('Average Clients in System')
plt.show()

plt.scatter(range(0, samplesize), theoryW)
plt.title('Theoretical W')
plt.xlabel('Arrival Rate')
plt.ylabel('Average Wait Time in System')
plt.show()

