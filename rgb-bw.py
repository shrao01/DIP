import cv2

# Read image
img = cv2.imread('E:\dip\d.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a black and white image
_, black_and_white = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the original image and the black and white image
cv2.imshow("Original Image", img)
cv2.imshow("Black and White Image", black_and_white)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()