import os
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'bear.png')  
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

# convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply a global threshold to the image
ret, thresh = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY)
# (source image, threshold value, max value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types, thresholding type)

cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Global Thresholding', thresh)
cv2.waitKey(0)