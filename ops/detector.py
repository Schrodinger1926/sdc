import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

from utils import validator


def get_canny_edge_mask(image, kernel_size, low_threshold, high_threshold):

    #convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Remove noise, perfrom gaussian smoothing
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
    # Type cast
    blur_gray_copy = blur_gray.astype(np.uint8)
    print(blur_gray_copy[])
    #find connect pixels with grad in b/w both ranges
    edges = cv2.Canny(blur_gray_copy, low_threshold, high_threshold)

    return edges


"""
if __name__ == "__main__":
    edges = get_canny_edge_mask(filename = "exit-ramp.png",
                                kernel_size = 3,
                                low_threshold = 100,
                                high_threshold = 200)
"""
