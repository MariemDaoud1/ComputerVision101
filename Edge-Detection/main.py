import os
import cv2
import numpy as np

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'cat.png')  
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

image_edged = cv2.Canny(image, 100, 200)
image_edged2 = cv2.Canny(image, 50, 150)

image_edged_d = cv2.dilate(image_edged, np.ones((5,5)))
image_edged_e  = cv2.erode(image_edged, np.ones((1,1)))

cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected Image', image_edged)
cv2.imshow('Edge Detected Image 2', image_edged2)
cv2.imshow('Dilated Edge Image', image_edged_d)
cv2.imshow('Eroded Edge Image', image_edged_e)
cv2.waitKey(0)