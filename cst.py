# Give a continuous function for implementing the contrast stretching transformation shown in Fig. 3.2(a) (3rd edition). 
# In addition to k, your function must include a parameter, E, for controlling the slope of the function as it transitions from low to high gray-level values. 
# Your function should be normalized (between 0 and 1 or 0 and 255)

import numpy as np
import matplotlib.pyplot as plt

# Number of gray levels in the image
L = 256  # This is typical for an 8-bit image

# Fixed value of k
k = L / 2

# Define a range of E values
E_values = [0.1, 0.5, 1.0, 2.0, 10.0]

# Input pixel values (ranging from 0 to L - 1)
r = np.arange(0, L, 1)

# Create subplots for each E value
plt.figure(figsize=(12, 6))
for E in E_values:
    # Calculate the contrast-stretched values for the given E
    s = 1 / (1 + (k / r) ** E)
    
    # Plot the transformation function for the current E
    plt.plot(r, s, label=f'E={E}')

# Plot the binary transformation (for E = infinity)
binary_s = np.where(r > k, 1.0, 0.0)
plt.plot(r, binary_s, label='Binary (E=∞)', linestyle='--', color='black')

# Customize the plot
plt.xlabel('Input Pixel Value (r)')
plt.ylabel('Output Pixel Value (s)')
plt.title('Family of Contrast Stretching Transformations for Different E Values')
plt.legend()
plt.grid()

# Show the plot
plt.show()