import cv2

# read webcam

webcam = cv2.VideoCapture(0) # 0 is the default camera


# visualize webcam

while True:
    ret, frame = webcam.read()
    if ret:
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'): # wait 1 ms between frames, press 'q' to quit
            break

# release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()