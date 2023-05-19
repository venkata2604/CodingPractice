# import cv2
#
# vidcap = cv2.VideoCapture("input/XND_Maintenance_Detection.mp4")
#
#
# def getFrame(sec):
#     vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
#     hasFrames,image = vidcap.read()
#     if hasFrames:
#         cv2.imwrite("out_img/image"+str(count)+".jpg", image)     # save frame as JPG file
#     return hasFrames
#
#
# sec = 0
# frameRate = 0.5  # it will capture image in each 0.5 second
#
#
# count = 1
#
# success = getFrame(sec)
# print(success)
#
# while success:
#     count = count + 1
#     sec = sec + frameRate
#     sec = round(sec, 2)
#     success = getFrame(sec)

# import sys
# mx = sys.maxsize
# print(mx)


labelling = [195, 39, 10, 20]
eol = [307, 116, 18, 22]

r = {"labelling": labelling, "eol": eol}

for key, value in r.items():
    if key == "labelling":
        print(value)

