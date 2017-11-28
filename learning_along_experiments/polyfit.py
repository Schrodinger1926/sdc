"""
Playing with numpy method polyfit

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from math import floor

img = mpimg.imread("assets/herb.png")
# lets make tick mark on it
img_tick_copy = np.copy(img)

# make the wierd fourth frame go away
img_tick_copy = img_tick_copy[:,:,:3]
plt.imshow(img_tick_copy)

# 				#
#			  #   
#           #
#         #
#    #  #          
#     #            

left_corner = (0, floor(0.75*img.shape[1]))
mid_corner = (floor(0.25*img.shape[0]), img.shape[1])
right_corner = (img.shape[0], 0)

# Draw these two intersecting lines on image
xx, yy = np.meshgrid(np.arange(0, img.shape[0]), np.arange(0, img.shape[1]))

# fit y(x) =  m*x + c
fit_left = np.polyfit(x = (left_corner[0], mid_corner[0]), y = (left_corner[1], mid_corner[1]), deg = 1)
fit_right = np.polyfit(x = (mid_corner[0], right_corner[0]), y = (mid_corner[1], right_corner[1]), deg = 1)

region_thresholds = ((yy > fit_left[0]*xx + fit_left[1] - 10) & (yy < fit_left[0]*xx + fit_left[1] + 10)) | \
					((yy > fit_right[0]*xx + fit_right[1] - 10) & (yy < fit_right[0]*xx + fit_right[1] + 10))

img_tick_copy[region_thresholds, :] = 0

plt.imshow(img_tick_copy)
plt.show()	