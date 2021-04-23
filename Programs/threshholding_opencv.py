import cv2 as cv
import numpy as np

img = cv.imread('newspaper.jpeg')

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# img2 = cv.dilate(th3, kernel=np.ones((2, 2), np.uint8))
# img3 = cv.erode(img2, kernel=np.ones((2, 2), np.uint8))

cv.imshow("Image", img)

cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
# cv.imshow("th4", img3)

cv.waitKey(0)
cv.destroyAllWindows()

