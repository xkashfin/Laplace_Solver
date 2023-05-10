import numpy as np

# Define problem parameters
L = 1  # length of domain
N = 100  # number of grid points
dx = L / (N-1)  # grid spacing
x = np.linspace(0, L, N)  # grid points
phi = np.zeros(N)  # initial solution guess

# Set boundary conditions
phi[0] = 0
phi[N-1] = 1

# Iterate until convergence
max_iter = 10000
tolerance = 1e-6
for k in range(max_iter):
    # Update phi using finite difference method
    for i in range(1, N-1):
        phi[i] = 0.5*(phi[i+1] + phi[i-1])

    # Check for convergence
    residual = np.abs(phi[1:-1] - 0.5*(phi[:-2] + phi[2:])).max()
    if residual < tolerance:
        print(f'Converged in {k} iterations with residual {residual}')
        break

# Plot solution
import matplotlib.pyplot as plt
plt.plot(x, phi)
plt.xlabel('x')
plt.ylabel('phi')
plt.show()
