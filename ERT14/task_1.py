import numpy as np
import matplotlib.pyplot as plt

# Data
V = np.array([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1])
v_out = np.array([1e-1, 1, 10, 15, 15, 15])

# Split the data into two ranges: under and over 1 mV
V_under_1mV = V[V < 1e-3]
v_out_under_1mV = v_out[V < 1e-3]

# Fit a linear model for V < 1mV
coefficients1 = np.polyfit(V_under_1mV, v_out_under_1mV, 1)
A1, B1 = coefficients1

# Create the linear model for V < 1mV
V_out_linear = A1 * V_under_1mV + B1

# For V > 1mV, use a constant value of 15
V_over_1mV = V[V >= 1e-3]
V_out_constant = np.full_like(V_over_1mV, 15)

# Combine the two models
predicted_v_out = np.concatenate((V_out_linear, V_out_constant))

# Plot the original data and the model
plt.scatter(V, v_out, label="Data")
plt.plot(V, predicted_v_out, label="Model", color='red')
plt.xlabel('V')
plt.ylabel('V_out')
plt.title('V_out vs V (Two-Part Model)')
plt.legend()
plt.show()

# Display the model parameters
print(f"Linear Model (V < 1mV): V_out = {A1:.4f} * V + {B1:.4f}")
print("Constant Model (V >= 1mV): V_out = 15")
