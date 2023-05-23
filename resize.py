import cv2
import numpy as np

# Read image
img = cv2.imread('E:\dip\d.jpg')

def resize(image, width=None, height=None):
    if width is not None and height is not None:
        return cv2.resize(image, (width, height))
    elif width is not None:
        height = int(image.shape[0] * (width / image.shape[1]))
        return cv2.resize(image, (width, height))
    elif height is not None:
        width = int(image.shape[1] * (height / image.shape[0]))
        return cv2.resize(image, (width, height))

resized_image = resize(img, width=800)
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()