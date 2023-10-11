"""
Program to plot the v_out of a op-amp circuit
"""

import numpy as np
import matplotlib.pyplot as plt

V = [1e-6, 1e-5, 1e-4, 1e-4, 1e-3, 1e-2, 1e-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
v_out = [3e-6, 3e-5, 3e-4, 3e-4, 3e-3, 3e-2, 3e-1, 3, 6, 9, 12, 15, 15, 15, 15, 15]

# Plotting the graph
plt.plot(V, v_out, 'ro')
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Op-amp circuit')
plt.grid(True)
plt.show()
