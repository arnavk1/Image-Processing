import  cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5)) # dissolve noise and smooths edges
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5) #here kernel size will be odd used for salt and pepper dots
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) #highly effective in noise removal while keeping edges sharp


titles = ['image', '2DConvulation', 'blur', 'gblur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

