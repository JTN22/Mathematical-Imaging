# Consider the noisy X-ray image of a circuit board corrupted by salt-and-pepper noise. 
# Filter this image by applying a linear average filter with a 3×3 mask (use the average mask with entries w_s,t = 1/9 , for all s, t ∈ {−1, 0, 1}). 
# You can keep the border pixels unchanged.

import cv2
import numpy as np

def apply_average_filter(image, kernel_size=3):
    # Create a kernel for the average filter
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

    # Apply the filter to the image
    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

def main():
    # Load the noisy image
    noisy_image = cv2.imread('noisy_circuit_board.png', cv2.IMREAD_GRAYSCALE)

    if noisy_image is None:
        print("Image not found or couldn't be loaded.")
        return

    # Apply the average filter
    filtered_image = apply_average_filter(noisy_image)

    # Display the original and filtered images
    cv2.imshow('Noisy Image', noisy_image)
    cv2.imshow('Filtered Image', filtered_image)

    # Save the filtered image if needed
    # cv2.imwrite('filtered_circuit_board.png', filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()