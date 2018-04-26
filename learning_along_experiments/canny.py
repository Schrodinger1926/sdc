import os

import matplotlib.pyplot as plt
import matplotlib.image as mimg
import cv2

ASSETS = 'assets'
image = mimg.imread('profile.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#cv2.imshow('title', image_gray)
low_threshold, high_threshold = 100, 250
image_edge = cv2.Canny(image_gray, low_threshold, high_threshold)
cv2.imwrite('output.jpg', image_edge)

#plt.imshow(image_edge)
