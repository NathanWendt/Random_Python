import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(-1.0, 1.0, 0.01)
s = np.power(t,2)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
