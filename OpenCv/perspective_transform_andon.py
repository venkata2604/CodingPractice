import cv2
import numpy as np

def return_perspecitve_transform(H, W):
    # Read the points from the yaml file (for now, hard coding)
    # points = []
    # src = np.float32([[11, 970], [1270, 970], [963, 101], [445, 93]])
    # src = np.float32([[187, 62], [214, 64], [215, 39], [187, 35]])
    # src = np.float32([[164, 83], [190, 87], [181, 59], [206, 62]])  # Labelling
    src = np.float32([[309, 156], [368, 180], [351, 122], [302, 102]])  # eol
    dst = np.float32([[0, H], [W, H], [W, 0], [0, 0]])
    perspective_transform = cv2.getPerspectiveTransform(src, dst)
    # using next 3 points for horizontal and vertical unit length(in this case 180 cm)
    pts = np.float32([[[236, 409], [249, 325]]])  # y - axis
    pts = np.float32([[[236, 409], [175, 386]]])  # x - axis
    warped_pt = cv2.perspectiveTransform(pts, perspective_transform)[0]
    distance = np.sqrt((warped_pt[0][0] - warped_pt[1][0]) ** 2 + (
            warped_pt[0][1] - warped_pt[1][1]) ** 2)

    return perspective_transform, warped_pt, distance


def get_transformed_points(box, perspective_transform):
    pnts = np.array([[[int(box[0]), int(box[1])]]], dtype="float32")

    # transforming yolo bottom mid pts to respective roi transformations
    trans_pnt_of_roi_1 = cv2.perspectiveTransform(pnts, perspective_transform)[0][0]

    pnt1 = [int(trans_pnt_of_roi_1[0]), int(trans_pnt_of_roi_1[1])]
    print(f"transformed points: {pnt1}")

    return pnt1


def roi_andon(point, perspective_transform):
    point = np.array([[[int(point[0]), int(point[1])]]], dtype="float32")
    trans_pnt_roi = cv2.perspectiveTransform(point, perspective_transform)[0][0]

    return trans_pnt_roi


def cal_dis(p1, p2, distance_x, distance_y):
    h = abs(p2[1] - p1[1])
    w = abs(p2[0] - p1[0])

    dis_w = float((w / distance_x) * 100)
    dis_h = float((h / distance_y) * 100)

    d = int(np.sqrt(((dis_h) ** 2) + ((dis_w) ** 2)))

    return d


# p = [268, 215]
# p = [215, 322]
p = [84, 300]
q = [316, 127]  # eol
# q = [200, 45]  # labelling
perspective_transform, warped_pt_x, warped_pt_y, distance_x, distance_y = return_perspecitve_transform(416, 416)
p1 = get_transformed_points(p, perspective_transform)  # p
p2 = roi_andon(q, perspective_transform)  # q

maint_dist = cal_dis(p1, p2, distance_x, distance_y)
print(maint_dist)
