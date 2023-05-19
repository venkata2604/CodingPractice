import cv2
import numpy as np


def hasYellow(frame_crop, low_value, high_value):
    hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
    col_mask = cv2.inRange(hsv_frame, low_value, high_value)
    output = cv2.bitwise_and(frame_crop, frame_crop, mask=col_mask)
    hasColor_sum = np.sum(col_mask)
    print(f"hascolorsum:{hasColor_sum}")
    # print("Green:" + str(hasColor_sum))
    if hasColor_sum > 100:
        print("YELLOW DETECTED")
        hasColor_flag = True
    else:
        print("YELLOW NOT DETECTED")
        hasColor_flag = False

    # cv2.imshow("Frame", frame_crop)
    # cv2.imshow("Mask", col_mask)
    # cv2.imshow("Frame_bitwise", output)

    return hasColor_flag, hasColor_sum


cap = cv2.VideoCapture("/home/venkata/Projects/input_data/REDlight_XND-6080RV_20210303081611.avi")

list_sum = []

while True:
    ret, frame = cap.read()
    r = [280+70, 290, 21, 70]
    # r1 = [435+100, 130+40, 30, 60]
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
    has_color_flag, color_sum = hasYellow(frame_crop, low_yellow_value, high_yellow_value)
    print(" sum of colour: ", color_sum)

    list_sum.append(color_sum)

    cv2.imshow("output video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()


print(list_sum)
minimum_sum = min(list_sum)
print("minimum sum", minimum_sum)
maximum_sum = max(list_sum)
print("maximum sum: ", maximum_sum)
