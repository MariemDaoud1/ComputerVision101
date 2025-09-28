import os
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'cat.png')  #__file__ → special variable that contains the path of the current script
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

# apply a blurring effect to the image
k_size = 7
blurred_image = cv2.blur(image, (k_size, k_size)) # (width, height)  // kernel size should be odd numbers


# apply a Gaussian blurring effect to the image
gaussian_blurred_image = cv2.GaussianBlur(image, (k_size, k_size), 0) # (width, height)  // kernel size should be odd numbers
cv2.imshow('Original Image', image)

# apply a median blurring effect to the image
median_blurred_image = cv2.medianBlur(image, k_size) # kernel size should be odd numbers
cv2.imshow('Blurred Image', blurred_image)  
cv2.imshow('Gaussian Blurred Image', gaussian_blurred_image)
cv2.imshow('Median Blurred Image', median_blurred_image)
cv2.waitKey(0)