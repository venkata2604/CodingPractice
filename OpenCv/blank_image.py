import cv2
import numpy as np


w = int(1920/4)
h = int(1080/4)

image = np.zeros((h, w, 3), np.uint8) #  empty image with given h and w

cv2.imshow("image", image)

cv2.waitKey(0)