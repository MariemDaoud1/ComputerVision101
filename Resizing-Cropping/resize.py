import os
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'cat.png')  #__file__ → special variable that contains the path of the current script
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

# resize the image to a specific width and height
resized_image = cv2.resize(image, (640, 200)) # (width, height)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)