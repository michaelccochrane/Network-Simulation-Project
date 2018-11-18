import random
import matplotlib.pyplot as plt

x = [round(random.random(), 3) for _ in range(1000)]
plt.hist(x)
plt.show()
