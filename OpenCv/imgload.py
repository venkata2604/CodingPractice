# reading a particular image

import cv2

# colored image 1 represents colour and 0 represnts grayscale
imgcolor = cv2.imread ("D:\Downloads\lisavicari.jpg", 1)
print("color array", imgcolor)
print(type(imgcolor))
cv2.imshow("beautiful", imgcolor)
cv2.waitKey(2000)
cv2.destroyAllWindows()


imggscale = cv2.imread ("D:\Downloads\lisavicari.jpg", 0)
print("Grayscale array:", imggscale)
print(type(imggscale))
print(imgcolor.shape)
print(imggscale.shape)
cv2.imshow("beautiful in black", imggscale)
cv2.waitKey(1000)  # if we enter 0 in there the window closes as soon as user presses any button
# where as if we give any value in that, window will stay for that particular number of milliseconds
cv2.destroyAllWindows()  # closes as per the waitkey parameter


