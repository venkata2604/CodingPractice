import numpy as np
import cv2

img = np.zeros((3, 3))
img[0:2, 2:4] = 120
img[1:3, 5:7] = 12
img[3:5, 0:2] = 5
img[5:7, 4:6] = 6
print(img)

cv2.imwrite('gray_img.jpg', img)
cv2.imshow('gray image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


