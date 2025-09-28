import cv2
import os

# # Read an image from file

image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'cat.png')  #__file__ → special variable that contains the path of the current script
image_path = os.path.abspath(image_path)

# # Write the image to a new file

image = cv2.imread(image_path)
cv2.imwrite(os.path.join(os.path.dirname(__file__), '..', 'images', 'cat_copy.png'), image)

# Visualize the image 
cv2.imshow('Cat', image)
cv2.waitKey(0) # Wait for a key press to close the window  // without this line, the window will close immediately