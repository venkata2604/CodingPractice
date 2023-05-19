import cv2
import numpy as np

cap = cv2.VideoCapture("/home/venkata/Projects/input_data/REDlight_XND-6080RV_20210303081611.avi")
list_sum = []

while True:
    ret, frame = cap.read()
    # frame = cap
    # orig = frame.copy
    r = [280+70, 290, 21, 70]
    # r = [145, 237, 30, 40]  # No light condition
    # r = [435+100, 130+40, 30, 60]
    # r = r1
    frame_crop = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    cv2.imshow("Cropped frame", frame_crop)
    cv2.rectangle(frame, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (0, 0, 255), 1)
    low_yellow_value = np.array([25, 50, 180])
    high_yellow_value = np.array([35, 255, 255])
    # low_yellow = np.array([25, 50, 180])
    # hig_yellow = np.array([35, 255, 255])
    low_red_value = np.array([96, 152, 245])
    high_red_value = np.array([179, 255, 255])
    gray = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)
    # minval, macval, minloc, maxLoc = cv2.minMaxLoc(gray)
    # minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    # cv2.circle(frame, maxLoc, 5, (255, 0, 0), 2)
    # display the results of the naive attempt
    # cv2.imshow("Naive", image)
    # apply a Gaussian blur to the image then find the brightest
    # region
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    print("maxloc", maxLoc)

    image = frame



    check_frame = frame_crop[int(maxLoc[1]-5):int(maxLoc[1] + 5), int(maxLoc[0]-5):int(maxLoc[0] + 5)]
    cv2.imshow("check frame: ", check_frame)
    cv2.circle(frame_crop, maxLoc, 2, (255, 0, 0), 2)
    # display the results of our newly improved method
    cv2.imshow("Robust", frame_crop)
    # has_color_flag, color_sum = hasYellow(frame_crop, low_yellow_value, high_yellow_value)
    # print(" sum of colour: ", color_sum)

    # list_sum.append(color_sum)

    cv2.imshow("output video", frame)
    # cv2. waitKey(0) # for image
    if cv2.waitKey(1) & 0xFF == ord('q'): break  # for video

cap.release()  # for video
cv2.destroyAllWindows()
