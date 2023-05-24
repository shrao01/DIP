import numpy as np
import cv2 as cv
img = cv.imread('E:\dip\d.jpg', 0)
img = cv.resize(img, (300,200))
 # Laplacian image gradient
lap = np.uint8(np.absolute(cv.Laplacian(img,cv.CV_64F, ksize=1)))
 # display the images
cv.imshow('Original', img)
cv.imshow('Lpalacian', lap)
cv.waitKey(0)
cv.destroyAllWindows()