# (Composite Laplacian Mask). 
# Write a computer program that implements the operation g(x, y) = f(x, y) − ∇2f(x, y) in the form of a spatial linear filter with a 3x3 mask. 
# Give the form of the mask and apply the program to the image of the North Pole of the Moon (Fig3.40(a).jpg). 
# You should turn in the details of the method, the computer program, the input and output images. 
# Perform your calculations only for interior pixels, not for boundary pixels. 
# Explain your result.

import cv2
import numpy as np

# Load the input image
input_image = cv2.imread('Fig3.40(a).jpg', cv2.IMREAD_GRAYSCALE)

# Define the composite Laplacian mask
composite_laplacian_mask = np.array([[-1, -1, -1],
                                     [-1, 9, -1],
                                     [-1, -1, -1]], dtype=np.float32)

# Apply the composite Laplacian filter
result_image = cv2.filter2D(input_image, -1, composite_laplacian_mask)

# Save the output image
cv2.imwrite('result_image.jpg', result_image)

# Display the original and result images
cv2.imshow('Original Image', input_image)
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()