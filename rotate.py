# import required libraries
import cv2

# load the input image
img = cv2.imread('E:\dip\d.jpg')

# rotate the image by 180 degree clockwise
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)

# display the rotated image
cv2.imshow("Image rotated by 180 degree", img_cw_180)
cv2.waitKey(0)
cv2.destroyAllWindows()