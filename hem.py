# Download Fig. 3.8(a) and perform histogram equalization on it (the MRI of a fractured human spine).
# As a minimum, your project solution should include the original image, a plot of its histogram, a plot of the histogram-equalization transformation function, the enhanced image, and a plot of its histogram. 
# Use this information to explain why the resulting image was enhanced as it was.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram of the original image
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# Calculate the cumulative distribution function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Perform histogram equalization
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# Apply the equalization to the image
equalized_image = cdf[image]

# Plot the original image, its histogram, equalization function, enhanced image, and its histogram
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Original Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(2, 3, 3)
plt.plot(cdf_normalized, color='b')
plt.title('CDF of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('CDF')

plt.subplot(2, 3, 4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()