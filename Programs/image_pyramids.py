import cv2 as cv
import numpy as np

img = cv.imread("lena.jpg")

# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)
# hr1= cv.pyrUp(lr2)
# instead of doing one by one use this; this is gaussian pyramid

layer = img.copy()
gpr = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gpr.append(layer)
    cv.imshow(str(i), layer)

# laplasian pyramid

layer = gpr[5]  #last image or top image
cv.imshow("gaussian upper level pyramid", layer)
lpr = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gpr[i])
    laplacian = cv.subtract(gpr[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)

cv.imshow("original image", img)
# cv.imshow("Pyrdown1 image", lr1)
# cv.imshow("Pyrdown2 image", lr2)
# cv.imshow("Pyrup1 image", hr1)

cv.waitKey(0)
cv.destroyAllWindows()