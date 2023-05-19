import cv2
import glob
vidcap = cv2.VideoCapture('/home/venkata/Projects/input_data/TIJ_small_repair.mp4')
# vidcap = [cv2.VideoCapture(file) for file in glob.glob("input/*.mp4")]

# for i in vidcap:
#     print(i)
#     while(True):
#         # Capture frame-by-frame
#         ret, frame = i.read()
#
#         # Our operations on the frame come here
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         # Display the resulting frame
#         cv2.imshow('frame',gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# # When everything done, release the capture
# i.release()
# cv2.destroyAllWindows()
# print(vidcap)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("out_img/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


sec = 0
frameRate = 0.5  # it will capture image in each 0.5 second


count = 66

success = getFrame(sec)
print(success)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
