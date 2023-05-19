# $ python mouse_click_corodinates.py --path /home/venkata/Projects/input_data/for_roi.png
import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--path", required=True)
args = vars(ap.parse_args())
# temp_list_of_coordinates = []

list_of_coordinates = []


def clickevent(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:

        print(x, ' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(img, str(x) + ',' + str(y), (x, y), font,  0.5, (0, 0, 255), 1)

        # cv2.imshow("Image", img)

        a = [x, y]

        list_of_coordinates.append(a)

        return list_of_coordinates


if __name__ == "__main__":
    # reading the image
    img = cv2.imread(args["path"])
    width = img.size
    print("width", width)

    # result = cv2.resize(img, (416 * 2, 416 * 2))
    # cv2.imshow('Image', result)

    cv2.imshow('Image', img)

    list_of_coordinates = []

    for i in range(0, 3):
        cv2.setMouseCallback('Image', clickevent)

    cv2.waitKey(0)

    # cv2.destroyAllWindows()

    print("list of coordinates:", list_of_coordinates)


