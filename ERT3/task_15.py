"""
Program to plot results from a totem (transistors)
"""
import matplotlib.pyplot as plt

Vq = [21, 27, 100, 300, 416, 514, 600, 646] # mV
Va = [0, 0.772, 1.112, 1.608, 2.02, 2.42, 2.76, 3.95] # V

plt.plot(Vq, Va, 'ro')
plt.xlabel('Vq (mV)')
plt.ylabel('Va (V)')
plt.show()
