import sys
import os
import argparse

import numpy as np
import cv2

from ops import detector

parser = argparse.ArgumentParser()
required_args = parser.add_argument_group("Required arguments")
required_args.add_argument('-i', '--input', required = True )
required_args.add_argument('-o', '--output', required = True)
args = parser.parse_args()

# HACKY ARCHITECHTURE
filename = args.input

image = cv2.imread(filename)

# Get canny edges
edges = detector.get_canny_edge_mask(image = image,
                                            kernel_size = 5,
                                            low_threshold = 50,
                                            high_threshold = 150)

# Next we'll create a masked edges image using cv2.fillPoly()
mask = np.zeros_like(edges)
ignore_mask_color = 255

# This time we are defining a four sided polygon to mask
imshape = image.shape
vertices = np.array([[(imshape[1]*0.08, imshape[0]*1),
                      (imshape[1]*0.48, imshape[0]*0.5),
                      (imshape[1]*0.52, imshape[0]*0.5),
                      (imshape[1]*0.92, imshape[0]*1)]], dtype=np.int32)

cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)

# Feed canny edge pixel to hough transform
rho = 2
theta = 1*(np.pi/180)
threshold = 200
min_line_length = 200
max_line_gap = 30
line_image = np.copy(image)*0

lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                     min_line_length ,max_line_gap)

assert(lines is not None),"No lines detected at all"
# Draw lines onto image copy
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

color_edges = np.dstack((edges, edges, edges))
combo = cv2.addWeighted(color_edges, 1, line_image, 1, 0)
cv2.imwrite(args.output, combo)
