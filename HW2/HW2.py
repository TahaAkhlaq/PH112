import matplotlib.pyplot as plt
import numpy as np

v = 6
vp = 2
a = 2
t0 = 0

def car_pos(t,v):
    return v * t

def pol_car_pos(t, vp, a, t0):
    return (vp * t) + (.5 * (a * (t - t0)**2))
  
# --------------- Plotting Prob 2.4c ----------------------

t = np.linspace(0, 5, 200)

x_car = car_pos(t, v)
x_police = pol_car_pos(t, vp, a, t0)

fig, ax = plt.subplots()
plt.plot(t, x_car, color='red', label = 'Car')
plt.plot(t, x_police, color='blue', label = 'Police Car')
#plt.xlim([0, 3])
#plt.ylim([0, 0.6])
ax.set(xlabel='time(sec)', ylabel='Position(m)')
ax.grid()
plt.legend(loc = 'upper left')
ax.set(title='Problem 2.4c')

# plt.savefig('Akhlaq Taha.pdf')
plt.show() 