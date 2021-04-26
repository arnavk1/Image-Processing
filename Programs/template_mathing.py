import cv2
import numpy as np


img = cv2.imread('messi5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('messi_temp.jpg', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)

thresh = 0.9
loc = np.where(res >= thresh)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()