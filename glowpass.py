# Implement the Gaussian lowpass filter in Eq. (4.3-8), using a radius D_0 = 25, and apply the algorithm to Fig4.11(a)

import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image (replace 'image_path' with your image file)
image = cv2.imread('image_path', 0)

# Apply Fourier Transform
f_transform = np.fft.fft2(image)
f_shift = np.fft.fftshift(f_transform)

# Calculate the frequency domain coordinates
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

# Radius D0
D0 = 25

# Create a meshgrid for frequency domain coordinates
u, v = np.meshgrid(np.arange(-ccol, cols - ccol), np.arange(-crow, rows - crow))

# Calculate the Euclidean distance
D = np.sqrt(u**2 + v**2)

# Gaussian lowpass filter
H = np.exp(- (D**2) / (2 * (D0**2)))

# Apply the filter
filtered_f_shift = f_shift * H

# Inverse Fourier Transform
filtered_f = np.fft.ifftshift(filtered_f_shift)
filtered_img = np.fft.ifft2(filtered_f)
filtered_img = np.abs(filtered_img)

# Display original and filtered images
plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(122)
plt.title('Filtered Image')
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()