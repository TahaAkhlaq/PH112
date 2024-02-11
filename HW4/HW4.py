import matplotlib.pyplot as plt
import numpy as np

# --------------- Plotting Prob 4.2f ----------------------

alpha = np.linspace(0, 20, 100)  
cos_values = (-alpha + np.sqrt(alpha**2 + 4)) / 2

plt.plot(alpha, cos_values, label=r'$\cos(\theta) = \frac{-\alpha + \sqrt{\alpha^2 + 4}}{2}$')
plt.legend(loc='upper right')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\cos(\theta)$')
plt.title('Function: cos(theta) as a function of alpha')
plt.grid(True)

plt.show()
