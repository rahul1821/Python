
import cv2
import numpy as np
img = cv2.imread("23.jpg")

blue_img = img[:,:,0] # blue color eliminate "0" means blue
green_img = img[:,:,1] # green color eliminate "1" means Green
red_img = img[:,:,2] # red color eliminate "2" means Red

new_img = np.hstack((blue_img,green_img,red_img)) # all images combine in a hstack tuple

cv2.imshow("Window", red_img)
cv2.waitKey(0)