import os
import cv2

# read an image from file
image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'whiteboard.png')  
image_path = os.path.abspath(image_path)
image = cv2.imread(image_path)
image = cv2.resize(image, (640, 400)) 

# draw a line on the image
cv2.line(image, (74,89), (40,40), (25,0,0), 5) 
# (start_point), (end_point), (B,G,R), thickness

# draw a rectangle on the image
cv2.rectangle(image, (150,150), (300,300), (0,255,0), 7)
# (top-left corner), (bottom-right corner), (B,G,R), thickness
# if thinkness = -1 → filled rectangle

# draw a circle on the image
cv2.circle(image, (400,200), 50, (0,0,255), 3)
# (center), radius, (B,G,R), thickness

# draw text on the image
cv2.putText(image, 'Hellooo', (400,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
# text, (bottom-left corner), font, font scale, (B,G,R), thickness

# visualize the image
cv2.imshow('Whiteboard', image)
cv2.waitKey(0)