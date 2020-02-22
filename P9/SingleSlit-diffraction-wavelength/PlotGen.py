import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

sin_arr = np.array([7.01E-03, 1.12E-02, 1.54E-02, 1.96E-02, 2.38E-02, 2.80E-02])
order = np.array([1, 2, 3, 4, 5, 6])

def y(x, m, c): return m * x + c
params, _ = optimize.curve_fit(y, order, sin_arr)

plt.plot(order, sin_arr, '--o', label='Experimental Data')
l2 = np.array((order[2], sin_arr[2]))

plt.title(r"n vs $sin(\Theta)$")
plt.text(l2[0], l2[1], 'y = {:.2E}x + {:.2E}'.format(*params), fontsize=12,
               rotation=36.5, rotation_mode='anchor')
plt.xlabel('n (order) ->')
plt.ylabel(r'$sin(\Theta)$ ->')
plt.legend()
plt.grid()
plt.savefig('plot.png')

