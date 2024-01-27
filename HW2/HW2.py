import matplotlib.pyplot as plt
import numpy as np

# --------------- Plotting Prob 2.4c ----------------------

t = np.linspace(0, 5, 200)
x = t
xpolice = (t*t)

fig, ax = plt.subplots()
plt.plot(t, x, color='red', label = 'Car')
plt.plot(t, xpolice, color='blue', label = 'Police Car')
#plt.xlim([0, 3])
#plt.ylim([0, 0.6])
ax.set(xlabel='time(sec)', ylabel='Position(m)')
ax.grid()
plt.legend(loc = 'upper left')

ax.set(title='Problem 2.4c')

plt.savefig('Akhlaq Taha.pdf')
plt.show()