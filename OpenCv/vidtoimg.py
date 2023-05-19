import cv2
vidcap = cv2.VideoCapture('/home/venkata/Projects/input_data/yellow to green mp.avi')


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite("/home/venkata/Projects/practice/outputimagesfromvideo/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


sec = 0
frameRate = 0.5  # it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    print("video writing success")
