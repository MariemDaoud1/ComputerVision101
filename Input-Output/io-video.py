import cv2
import os

# Read video from file


video_path = os.path.join(os.path.dirname(__file__), '..', 'videos', 'SpongeBob.mp4') 
video_path = os.path.abspath(video_path)
video = cv2.VideoCapture(video_path)

# # # Write the video to a new file

# Visualize the video 

ret = True
while ret:  
    ret, frame = video.read()
    if ret:
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Release the video capture object and close all OpenCV windows

video.release()
cv2.destroyAllWindows()


# video.release() frees the resources associated with the video file. This closes the file and avoids memory leaks.
# cv2.destroyAllWindows() closes all OpenCV windows that were opened with cv2.imshow(). This ensures your program exits cleanly and no windows are left open

