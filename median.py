# Write a computer program that will denoise an image using the 3x3 median filter. 
# Apply your algorithm to the X-Ray image of a circuit board corrupted by salt-and-pepper noise (Fig3.37(a).jpg). 
# You should turn in the details of the method, your computer program, the input and output images. 
# For simplicity, perform your calculations only for interior pixels, not for boundary pixels. 
# Explain your result and compare it with the output obtained using the linear average filter.

import cv2
import numpy as np

# Load the image
image = cv2.imread('Fig3.37(a).jpg', 0)  # Load the image in grayscale

# Define the size of the filter
filter_size = 3

# Define a function to apply the median filter
def median_filter(img, size):
    result = np.copy(img)
    offset = size // 2
    for i in range(offset, img.shape[0] - offset):
        for j in range(offset, img.shape[1] - offset):
            neighbors = img[i - offset:i + offset + 1, j - offset:j + offset + 1]
            result[i, j] = np.median(neighbors)
    return result

# Apply the median filter to the image
denoised_image = median_filter(image, filter_size)

# Save the denoised image
cv2.imwrite('denoised_image.jpg', denoised_image)

# Load and display the original and denoised images for comparison
original_image = cv2.imread('Fig3.37(a).jpg')
cv2.imshow('Original Image', original_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()