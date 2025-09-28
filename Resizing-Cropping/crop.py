import os
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'cat.png')  #__file__ → special variable that contains the path of the current script
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

# cropping the image
cropped_image = image[50:200, 200:400] # image[y1:y2, x1:x2] (height, width)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)