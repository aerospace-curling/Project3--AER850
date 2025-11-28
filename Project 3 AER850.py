#AER 850 Project 3
#EMILY PEELAR- 501169755

#importing the library for OpenCV
import cv2
#importing the numpy library
import numpy as np


#importing the image to be used through the OpenCV library
image = cv2.imread(r"Project 3 Data/Project 3 Data/motherboard_image.JPEG")

#importing the library to display plots
import matplotlib.pyplot as plt

#changing the image to grayscale so that it can be used in thresholding
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#showing the image in grayscale
plt.figure()
plt.imshow(gray_image, cmap='gray')
plt.title("Image in Grayscale")
plt.axis('off')
plt.show()

#adding gaussian blur to help differentiate between key features:
blur = cv2.GaussianBlur(gray_image, (5, 5),0)

#creating the binary threshold
_,threshold = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

#showing the image with the binary threshold
plt.figure()
plt.imshow(threshold, cmap='gray')
plt.title("Image with Binary Threshold")
plt.axis('off')
plt.show()

#using canny to detect edges
edges = cv2.Canny(threshold, 100, 200)
plt.figure()
plt.imshow(edges, cmap='gray')
plt.title("Image with Edges Defined with Canny")
plt.axis('off')
plt.show()

