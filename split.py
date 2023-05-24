import cv2
import numpy as np
import random

# Read image
img = cv2.imread('output_image.jpg')

# Specify the number of rows and columns for the grid
num_rows = 4
num_cols = 4

# Calculate the size of each grid cell
height, width, _ = img.shape
cell_height = height // num_rows
cell_width = width // num_cols

# Create a list of grid cell coordinates
cell_coords = [(i * cell_height, j * cell_width) for i in range(num_rows) for j in range(num_cols)]

# Shuffle the cell coordinates randomly
random.shuffle(cell_coords)

# Split the image into grid cells and save each cell as a separate image
for i, (y, x) in enumerate(cell_coords):
    cell_img = img[y:y+cell_height, x:x+cell_width]
    cv2.imwrite(f"image_{i}.jpg", cell_img)

    # Display each cell image
    cv2.imshow(f"Image {i}", cell_img)

# Display the original image
cv2.imshow("Original Image", img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()