import numpy as np
import cv2
import time

# Define the duration (in seconds) of the video capture here
capture_duration = 10

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()