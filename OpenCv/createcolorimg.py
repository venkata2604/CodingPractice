import numpy
import cv2

b = numpy.zeros([1024, 768, 3])

b[:, :, 0] = numpy.ones([1024, 768])*250
b[:, :, 1] = numpy.ones([1024, 768])*0
b[:, :, 2] = numpy.ones([1024, 768])*0

cv2.imwrite('color_img.jpg', b)
cv2.imshow('Color image', b)
cv2.waitKey(2000)
cv2.destroyAllWindows()
