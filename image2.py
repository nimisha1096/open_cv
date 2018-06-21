#!/usr/bin/python2
import cv2
img=cv2.imread('index.jpeg')
img1=cv2.imread('index1.jpeg',0)

print (img.shape)
print (img1.shape)

cv2.imshow("index",img)
cv2.imshow("indexnew",img1)

cv2.waitKey(0)

cv2.destroyAllWindows()

