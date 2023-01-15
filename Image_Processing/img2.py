import numpy as np
import cv2

img = cv2.imread("23.jpg")

# small_img = cv2.resize(img,(250,250)) # resize image

# crop_img = img[0:300,0:300]   # crop image
flip_img = cv2.flip(img, 0) # flip image bottom to up
flip_img1 = cv2.flip(img, 1) # flip image left to right
flip_img2 = cv2.flip(img, -1) # flip image bottom to up and left to right both
new_img = np.hstack((flip_img, flip_img1, flip_img2))
cv2.imshow("Window", new_img)
cv2.waitKey(0)