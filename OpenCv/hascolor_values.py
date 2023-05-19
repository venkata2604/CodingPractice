import cv2
import numpy as np


def hasred(frame_crop, low_value, high_value):
    hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
    col_mask = cv2.inRange(hsv_frame, low_value, high_value)
    output = cv2.bitwise_and(frame_crop, frame_crop, mask=col_mask)
    hasColor_sum = np.sum(col_mask)
    print("Green:" + str(hasColor_sum))
    if hasColor_sum > 100:
        print("DETECTED")
        hasColor_flag = True
    else:
        print("NOT DETECTED")
        hasColor_flag = False

    cv2.imshow("Frame", frame_crop)
    cv2.imshow("Mask", col_mask)
    cv2.imshow("Frame_bitwise", output)

    return hasColor_flag


img = cv2.imread("/home/venkata/Projects/practice/opencv/hascolor_values.py")
frame_crop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
#low_green = np.array([40, 0, 0])
#hig_green = np.array([179, 255, 255])
#hasColor_flag = hasGreen(frame_crop, low_green, hig_green)
low_yellow = np.array([25, 50, 180])
hig_yellow = np.array([35, 255, 255])
hasColor_flag = hasGreen(frame_crop, low_yellow, hig_yellow)