import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

print(img.shape) #returns tuple of rows, columns, channels
print(img.size) #return total no of pixels
print(img.dtype) #returns data type of image

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330: 390]
img[273:333, 100:160] = ball

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

