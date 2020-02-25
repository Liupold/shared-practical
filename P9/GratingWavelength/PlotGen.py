import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

sin_arr_1 = np.array([0.205445681662985, 0.40484279140067, 0.580944283147532])
sin_arr_2 = np.array([0.269380120342599, 0.497444986275752,\
        0.672672793996312, 0.849240578267352])

order_1 = np.array([1, 2, 3])
order_2 = np.array([1, 2, 3, 4])

def y(x, m, c): return m * x + c
# Plot1
params, _ = optimize.curve_fit(y, order_1, sin_arr_1)

plt.plot(order_1, sin_arr_1, '--o', label='Experimental Data')
l2 = np.array((order_1[1], sin_arr_1[1]))

plt.title(r"n vs $sin(\Theta)$ (set I)")
plt.text(l2[0], l2[1], 'y = {:.2E}x + {:.2E}'.format(*params), fontsize=12,
               rotation=36.5, rotation_mode='anchor')
plt.xlabel('n (order) ->')
plt.ylabel(r'$sin(\Theta)$ ->')
plt.legend()
plt.grid()
plt.savefig('plot1.png')
plt.close()

#Plot2
params, _ = optimize.curve_fit(y, order_2, sin_arr_2)

plt.plot(order_2, sin_arr_2, '--o', label='Experimental Data')
l2 = np.array((order_2[1], sin_arr_2[1]))

plt.title(r"n vs $sin(\Theta)$ (set II)")
plt.text(l2[0], l2[1], 'y = {:.2E}x + {:.2E}'.format(*params), fontsize=12,
               rotation=36.5, rotation_mode='anchor')
plt.xlabel('n (order) ->')
plt.ylabel(r'$sin(\Theta)$ ->')
plt.legend()
plt.grid()
plt.savefig('plot2.png')
