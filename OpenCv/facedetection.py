import cv2

# cascade classifier

# Create a Cascade Classfier object
face_cascade = cv2.CascadeClassifier("D:\\Downloads\\Haarcascade_xml_files\\haarcascade_frontalcatface.xml")


# Reading the image as it is
img = cv2.imread("D:\\Downloads\\lisa2.jpg")

# Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the co-ordinates of the image

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)


print(type(faces))
print(faces)


for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Gray", img)
    cv2.waitKey(0)
