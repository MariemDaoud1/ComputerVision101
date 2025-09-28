import os
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'birdss.png') 
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, image_t = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 100:
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 3)
        # draw each contour only if its area is greater than 100 pixels
        # (source image, contours, contour index (-1 to draw all contours), color (BGR), thickness)

        cv2.boundingRect(cnt) # get the bounding rectangle of the contour
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # draw the bounding rectangle around the contour
        
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', image_t)
cv2.waitKey(0)