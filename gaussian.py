import cv2
import numpy as np

# Read image
img = cv2.imread('E:\dip\d.jpg')

def gaussian_blur(image, kernel_size=(5,5), sigmaX=0):
    return cv2.GaussianBlur(image, kernel_size, sigmaX)

blurred_image = gaussian_blur(img, kernel_size=(21, 21), sigmaX=0)
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()