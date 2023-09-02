"""
Program to plot results from a totem (transistors)
"""
import matplotlib.pyplot as plt

Vq = [7.89, 7.89, 7.89, 7.88, 7.86, 7.76, 7.47, 2.96, 0.066, 0.005] # mV
Va = [0.5, 0.750, 1.00, 1.250, 1.500, 1.750, 2.0, 2.25, 2.32, 2.5] # V

plt.plot(Vq, Va, 'ro')
plt.xlabel('Vq (mV)')
plt.ylabel('Va (V)')
plt.show()
