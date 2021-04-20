import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, ', ', y)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = str(x) + ', ' + str(y)
        # cv2.putText(img, strXY, (x,y), font, .5, (255,255,0), 2)
        ##############################################
        # cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        # points.append((x, y))
        # if len(points) >= 2:
        #     cv2.line(img, points[-1], points[-2], (255,0,0), 3)
        ########################################################
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)
        mycolorImage[:] = [b, g, r]

        ###################################
        cv2.imshow('color', mycolorImage)
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     b = img[y, x, 0]
    #     g = img[y, x, 1]
    #     r = img[y, x, 2]
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strbgr = str(b) + ', ' + str(g) + ', ' + str(r)
    #     cv2.putText(img, strbgr, (x, y), font, .5, (0, 255, 255), 2)
    #     cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('baboon.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()

