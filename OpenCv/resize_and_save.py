import cv2
import numpy as np

img = cv2.imread("/home/venkata/Projects/input_data/82_markers_HD.jpg")
res = cv2.resize(img, (416, 416))
cv2.imwrite("../../input_data/82_marker_416.jpg", res)
