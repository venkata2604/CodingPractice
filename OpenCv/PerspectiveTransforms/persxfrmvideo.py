import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    print(frame.shape)  # to know the size of frame
    cv2.circle(frame, (155, 120), 5, (0, 0, 255), -1)  # indicate red dots to find edges of image
    cv2.circle(frame, (480, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (20, 475), 5, (0, 0, 255), -1)
    cv2.circle(frame, (620, 475), 5, (0, 0, 255), -1)

    pts1 = np.float32([[155, 120], [480, 120], [20, 475], [620, 475]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(frame, matrix, (500, 500))


    cv2.imshow("Frame", frame)
    cv2.imshow("prespective Transformation", result)

    key = cv2.waitKey(1)
    if key == 27:  # 27 corresponds to s in keyboard
        break

cap.release()
cv2.destroyAllWindows()
