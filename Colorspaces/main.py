import os 
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'cat.png')  
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

cv2.imshow('Original Image', image)
cv2.waitKey(0)

# convert the image to RGB (Red, Green, Blue)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image', rgb_image)
cv2.waitKey(0)

# convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)

# convert the image to HSV (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)

# convert the image to LAB (Lightness, A channel, B channel)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow('LAB Image', lab_image)
cv2.waitKey(0)