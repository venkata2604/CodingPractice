import cv2
import numpy as np


def hasRed(frame_crop, low_red_value, high_red_value):
    hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
    col_mask = cv2.inRange(hsv_frame, low_red_value, high_red_value)
    output = cv2.bitwise_and(frame_crop, frame_crop, mask=col_mask)
    hasRedColor_sum = np.sum(col_mask)
    cv2.imshow("Cropped frame", frame_crop)
    cv2.imshow("Mask", col_mask)
    cv2.imshow("Frame_bitwise", output)

    # print("Red:" + str(hasColor_sum))
    if hasRedColor_sum > 100:
        # print("YELLOW DETECTED")
        hasRed_flag = True
    else:
        # print("YELLOW NOT DETECTED")
        hasRed_flag = False
    return hasRedColor_sum, hasRed_flag


cap = cv2.VideoCapture("/home/venkata/Projects/input_data/REDlight_XND-6080RV_20210303081611.avi")

list_sum = []
while True:
    ret, frame = cap.read()
    # r = [173+40, 161+30, 21, 25+10]  # red
    r = [280 + 70, 290, 21, 70]  # yellow andon
    # r1 = [435+100, 130+40, 30, 60]
    # r = r1
    frame_crop = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    cv2.rectangle(frame, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (0, 0, 255), 1)
    # low_red_value = np.array([96, 152, 245])
    # high_red_value = np.array([179, 255, 255])
    # low_red_value = np.array([96, 152, 245])
    # high_red_value = np.array([179, 255, 255])

    # low_yellow = np.array([25, 50, 180])
    # hig_yellow = np.array([35, 255, 255])

    low_red_value = np.array([129, 185, 199])
    high_red_value = np.array([179, 255, 255])
    hasRedColor_sum, hasRed_flag = hasRed(frame_crop, low_red_value, high_red_value)
    print(" sum of colour: ", hasRedColor_sum)

    list_sum.append(hasRedColor_sum)

    cv2.imshow("output video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()


print(list_sum)
minimum_sum = min(list_sum)
print("minimum sum", minimum_sum)
maximum_sum = max(list_sum)
print("maximum sum: ", maximum_sum)
