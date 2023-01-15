import numpy as np
import cv2


img = cv2.imread("23.jpg") #read Image
# print(type(img))
# print(img.shape)  # image dimension and color channel
# cv2.imshow("window", img)  # image show from the path
# cv2.waitKey(0)  # hold the image screen


#RGB is a 3 channel image and grayscale image is a 2 channel image

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)
cv2.imshow("Window",img_gray)
cv2.waitKey(0)