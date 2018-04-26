import sys
import os
import argparse

import numpy as np
import cv2

from ops import detector

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')
args = parser.parse_args()

# HACKY ARCHITECHTURE
filename = args.input
image = cv2.imread(filename)

print(image.shape)

# Get canny edges
masked_edges = detector.get_canny_edge_mask(image = image,
                                            kernel_size = 5,
                                            low_threshold = 50,
                                            high_threshold = 150)


cv2.imwrite('output.jpg', masked_edges)
quit()
# Feed canny edge pixel to hough transform
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image)*0

lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                     min_line_length ,max_line_gap)

# Draw lines onto image copy
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

color_edges = np.dstack((masked_edges, masked_edges, masked_edges))

combo = cv2.addWeighted(color_edges, 0, line_image, 1, 0)
cv2.imwrite(args.output, combo)
