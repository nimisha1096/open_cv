#!/usr/bin/python2
import cv2
img=cv2.imread('index.jpeg')
print (img.shape)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

