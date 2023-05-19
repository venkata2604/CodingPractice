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
    pts_y = np.float32([[[236, 409], [249, 325]]])  # y - axis
    pts_x = np.float32([[[236, 409], [175, 386]]])  # x - axis
    warped_pt_x = cv2.perspectiveTransform(pts_x, perspective_transform)[0]
    warped_pt_y = cv2.perspectiveTransform(pts_y, perspective_transform)[0]
    distance_x = np.sqrt((warped_pt_x[0][0] - warped_pt_x[1][0]) ** 2 + (
            warped_pt_x[0][1] - warped_pt_x[1][1]) ** 2)
    distance_y = np.sqrt((warped_pt_y[0][0] - warped_pt_y[1][0]) ** 2 + (
            warped_pt_y[0][1] - warped_pt_y[1][1]) ** 2)
    return perspective_transform, warped_pt_x, warped_pt_y, distance_x, distance_y


def get_transformed_points(box, prespective_transform):
    pnts = np.array([[[int(box[0]), int(box[1])]]], dtype="float32")

    # transforming yolo bottom mid pts to respective roi transformations
    trans_pnt_of_roi_1 = cv2.perspectiveTransform(pnts, prespective_transform)[0][0]

    pnt1 = [int(trans_pnt_of_roi_1[0]), int(trans_pnt_of_roi_1[1])]

    return pnt1


def roi_andon(point, prespective_transform):
    point = np.array([[[int(point[0]), int(point[1])]]], dtype="float32")
    trans_pnt_roi = cv2.perspectiveTransform(point, prespective_transform)[0][0]

    return trans_pnt_roi


def cal_dis(p1, p2, distance_x, distance_y):
    h = abs(p2[1] - p1[1])
    w = abs(p2[0] - p1[0])

    dis_w = float((w / distance_x) * 100)
    dis_h = float((h / distance_y) * 100)

    print(f"euclidean dish: {dis_h}, {dis_w}")

    d = int(np.sqrt(((dis_h) ** 2) + ((dis_w) ** 2)))
    print(f"euclidean d : {d}")

    return d

def cal_dis_manhattan(p1, p2, distance_x, distance_y):
    h = abs(p2[1] - p1[1])
    w = abs(p2[0] - p1[0])

    dis_w = float((w / distance_x) * 100)
    dis_h = float((h / distance_y) * 100)

    # d = int(np.sqrt(((dis_h) ** 2) + ((dis_w) ** 2)))
    d = (dis_h + dis_w)
    print(f"manhattan dish: {dis_h}, {dis_w}")
    print(f"manhattan d : {d}")
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
maint_dist_manhattan = cal_dis_manhattan(p1, p2, distance_x, distance_y)
print("euclediaan", maint_dist)
print("manhattan", maint_dist_manhattan)
