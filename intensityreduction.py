# Write a computer program (with pseudocode) capable of reducing the number of intensity levels in an image from 256 to 2, in integer powers of 2. 
# The desired number of intensity levels needs to be a variable input to your program

from PIL import Image
import numpy as np

# Input the desired number of intensity levels
n = int(input("Enter the desired number of intensity levels (e.g., 2, 4, 8): "))

# Open the image
image = Image.open("input_image.jpg")

# Convert the image to grayscale
image = image.convert("L")

# Convert the image to a NumPy array
imageArray = np.array(image)

# Calculate the scaling factor
scaleFactor = 256 / (2**n)

# Create an empty array for the reduced image
reducedImageArray = np.zeros_like(imageArray)

# Reduce the number of intensity levels
for i in range(imageArray.shape[0]):
    for j in range(imageArray.shape[1]):
        pixelIntensity = imageArray[i, j]
        newIntensity = int(np.floor(pixelIntensity / scaleFactor) * scaleFactor)
        reducedImageArray[i, j] = newIntensity

# Create a reduced image from the reducedImageArray
reducedImage = Image.fromarray(reducedImageArray)

# Save the reduced image
reducedImage.save("reduced_image.jpg")

print("Image with", n, "intensity levels created and saved as reduced_image.jpg")