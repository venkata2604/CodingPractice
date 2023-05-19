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
        # print("YELLOW DETECTED")
        hasColor_flag = True
    else:
        # print("YELLOW NOT DETECTED")
        hasColor_flag = False

    # cv2.imshow("Frame", frame_crop)
    # cv2.imshow("Mask", col_mask)
    # cv2.imshow("Frame_bitwise", output)

    return hasColor_flag, hasColor_sum, col_mask, output


def hasRed(frame_crop, low_red_value, high_red_value):
    hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
    col_mask = cv2.inRange(hsv_frame, low_red_value, high_red_value)
    output = cv2.bitwise_and(frame_crop, frame_crop, mask=col_mask)
    hasRedColor_sum = np.sum(col_mask)
    # print("Red:" + str(hasColor_sum))
    if hasRedColor_sum > 100:
        # print("RED DETECTED")
        hasRed_flag = True
    else:
        # print("YELLOW NOT DETECTED")
        hasRed_flag = False
    return hasRed_flag, hasRedColor_sum, col_mask, output

# def hasGreen(frame_crop, low_green_value, high_green_value):
#     hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
#     col_mask = cv2.inRange(hsv_frame, low_red_value, high_red_value)
#     output = cv2.bitwise_and(frame_crop, frame_crop, mask=col_mask)
#     has_greenColor_sum = np.sum(col_mask)
#     # print("Red:" + str(hasColor_sum))
#     if has_greenColor_sum > 100:
#         # print("RED DETECTED")
#         has_green_flag = True
#     else:
#         # print("YELLOW NOT DETECTED")
#         has_green_flag = False
#     return has_green_flag, has_greenColor_sum, col_mask, output


cap = cv2.VideoCapture("/home/venkata/Projects/input_data/REDlight_XND-6080RV_20210303081611.avi")

list_sum = []

while True:
    ret, frame = cap.read()
    r = [280 + 70, 290, 21, 70]  # yellow andon
    # r = [173+40, 161+30, 21, 25+10]  # red andon
    # r = [1177, 250, 30, 45] # green andon left
    # r = [910, 85, 30, 50]  # green andon straight
    # r1 = [435+100, 130+40, 30, 60]
    # r = r1
    frame_crop = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    cv2.rectangle(frame, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (0, 0, 255), 1)
    # low_yellow_value = np.array([25, 50, 180])
    # high_yellow_value = np.array([35, 255, 255])
    low_yellow = np.array([25, 50, 180])
    hig_yellow = np.array([35, 255, 255])

    # low_red_value = np.array([96, 152, 245])
    # high_red_value = np.array([179, 255, 255]) ############ old

    low_red_value = np.array([129, 185, 199])
    high_red_value = np.array([179, 255, 255])



    # low_green_value = np.array([0, 0, 255])
    # high_green_value = np.array([0, 0, 255])

    # low_green_value = np.array([36, 0, 0])
    # high_green_value = np.array([86, 255, 255])

    low_value = low_yellow
    high_value = hig_yellow

    has_yellow_flag, yellow_color_sum, col_mask_yellow, output_yellow = hasYellow(frame_crop, low_value, high_value)
    has_red_flag, red_color_sum, col_mask_red, output_red = hasRed(frame_crop, low_value, high_value)
    # has_green_flag, green_color_sum, col_mask_green, output_green = hasGreen(frame_crop, low_value, high_value)

    cv2.imshow("Cropped frame", frame_crop)
    cv2.imshow("Mask", col_mask_yellow)
    cv2.imshow("Frame_bitwise", output_yellow)
    cv2.imshow("Frame_bitwise", output_red)



    print(f"has red flag", has_red_flag)
    print(f"has yellow flag ", has_yellow_flag)
    # print(f"red color sum: {red_color_sum}, yellow color sum: {yellow_color_sum}, green color sum: {green_color_sum}")

    if has_red_flag:
        print("red light detected")
    if has_yellow_flag:
        print("yellow light detected")
    # if has_green_flag:
    #     print("green light detected")

    # list_sum.append(color_sum)

    cv2.imshow("output video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
