# Download Fig5.26a and plot a gradient map g (or its “image negative”; edges will appear black, while homogenous regions will appear white; rescaling may be necessary). 
# Ignore the pixels on the boundary of the image for simplicity when computing the discrete gradient.

import cv2

# Load the image
image = cv2.imread('Fig5.26a.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute the gradient using Sobel operators
gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# Normalize the gradient magnitude
gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Save the gradient map as an image file
cv2.imwrite('gradient_map.jpg', gradient_magnitude_normalized)