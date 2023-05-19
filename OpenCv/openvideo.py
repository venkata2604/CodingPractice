import cv2
import numpy as np
import argparse

import time

ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--name", required=True,
                # help="name of the user")

ap.add_argument("-p", "--path", default="/home/venkata/Projects/input_data/TIJ_small_repair.mp4", required=True, help="name of the user")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["path"])

prev_frame_time = 0
new_frame_time = 0

while True:
    ret, frame = cap.read()

    new_frame_time = time.time()

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time

    # fps = str(fps)

    cv2.putText(frame, "Frame Rate: {}".format(str(fps)), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

    print(type(fps))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


