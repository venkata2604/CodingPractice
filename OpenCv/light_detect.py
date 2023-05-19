import cv2
import numpy as np
#cap = cv2.VideoCapture("TIJ_small.mp4")
cap = cv2.VideoCapture("TIJ_small_repair.mp4")
counter = 1

def hasColor(frame_crop, low_value, high_value):
    hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
    col_mask = cv2.inRange(hsv_frame, low_value, high_value)
    output = cv2.bitwise_and(frame_crop,frame_crop, mask = col_mask)
    hasColor_sum = np.sum(col_mask)
    print(hasColor_sum)
    if hasColor_sum > 0:
        print("DETECTED")
        hasColor_flag = True
    else:
        print("NOT DETECTED")
        hasColor_flag = False
    
    cv2.imshow("Frame",frame_crop)
    cv2.imshow("Mask", col_mask)
    cv2.imshow("Frame_bitwise",output)


    return hasColor_flag
    


while True:
    _, frame = cap.read()
    if counter==1:
        r = cv2.selectROI(frame)    
        frame_crop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    hsv_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2HSV)
    gray_frame = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)

    cv2.imshow("HSV",hsv_frame)
    cv2.imshow("GRAY",gray_frame)

    low_white = np.array([0,0,0])
    hig_white = np.array([0,0,255])

    low_red = np.array([161,155,84])
    hig_red = np.array([179,255,255])

    low_green = np.array([85,50,25])
    hig_green = np.array([90,100,255])

    low_yellow = np.array([25,50,180])
    hig_yellow = np.array([35,255,255])
    #mask = cv2.inRange(hsv_frame, low_red, hig_red)

    hasColor_flag = hasColor(frame_crop, low_yellow, hig_yellow)
    #hasColor_flag = hasColor(frame_crop, low_red, hig_red)
    #hasColor_flag = hasColor(frame_crop, low_white, hig_white)
    #hasColor_flag = hasColor(frame_crop, low_green, hig_green)
    counter = counter + 1
    key = cv2.waitKey(1)
    if key == 27:
        break







#green = np.uint8([[[0,255,0 ]]])
#hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
#print( hsv_green )
#[[[ 60 255 255]]]