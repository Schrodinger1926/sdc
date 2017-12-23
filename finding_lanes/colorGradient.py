import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


image = mpimg.imread("exit-ramp.png")

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# remove noise, perfrom gaussian smoothing
kernel_size = 3 # Aperture size k*k
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)


# diff in intensity value
low_threshold = 100
high_threshold = 200

# remove all below low_threshold
# Find ones with greater than high_threshold
# then find connect pixels with grad in b/w both ranges
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)


# plt.imshow(edges, cmap = "gray")
# plt.show()
