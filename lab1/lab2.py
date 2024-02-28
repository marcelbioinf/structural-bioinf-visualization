# import numpy as np
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt

# # Define the differential equation as a Python function
# def model(Y, t, beta, alpha):
#     dYdt = beta - alpha * Y
#     return dYdt

# # Initial condition
# Y0 = 0.0

# # Time points
# t = np.linspace(0, 80, 201)  # Define the time points from 0 to 10 with 101 intervals

# # Parameters
# beta = 0.72
# alpha = 0.07

# # Solve the differential equation using odeint
# Y = odeint(model, Y0, t, args=(beta, alpha))

# # Plot the results
# plt.plot(t, Y)
# plt.xlabel('Time (t)')
# plt.ylabel('Y(t)')
# plt.title('Solution of dY/dt = beta - alpha * Y')
# plt.grid(True)
# plt.show()


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation as a Python function
def model(Y, t, beta_func, alpha):
    # Obtain the current value of beta at the given time
    beta = beta_func(t)
    dYdt = beta - alpha * Y
    return dYdt

# Initial condition
Y0 = 0.0

# Time points
t = np.linspace(0, 10, 101)

# Parameter values
alpha = 0.1

# Define a function for beta that changes at a specific time point
def beta_func(t):
    if t < 5.0:
        return 0.7  # Initial value of beta
    else:
        return 0.51  # Updated value of beta after t = 5.0

# Solve the differential equation using odeint
Y = odeint(model, Y0, t, args=(beta_func, alpha))

# Plot the results
plt.plot(t, Y)
plt.xlabel('Time (t)')
plt.ylabel('Y(t)')
plt.title('Solution of dY/dt = beta - alpha * Y with changing beta')
plt.grid(True)
plt.show()
