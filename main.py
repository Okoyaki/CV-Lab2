import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def kp_detection(img, img_temp,i):
    input_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    reference_image = cv2.cvtColor(img_temp, cv2.COLOR_RGB2GRAY)
    
    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(reference_image, None)
    kp2, des2 = sift.detectAndCompute(input_image, None)

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    points1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    points2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    homography_matrix, mask = cv2.findHomography(points1, points2, cv2.RANSAC, 5.0)

    h, w = reference_image.shape
    corners = np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2)

    if homography_matrix is not None:
        transformed_corners = cv2.perspectiveTransform(corners, homography_matrix)

        x_min = int(min(transformed_corners[:, 0, 0]))
        y_min = int(min(transformed_corners[:, 0, 1]))
        x_max = int(max(transformed_corners[:, 0, 0]))
        y_max = int(max(transformed_corners[:, 0, 1]))

        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (255, 0, 0), 3)
    cv2.imwrite('data/result/kp/temp/img'+str(i)+'.jpg', img)


def temp_matching(img, img_temp,i):
    result = cv2.matchTemplate(img,img_temp, cv2.TM_CCOEFF_NORMED)

    (minv, maxv, minl, maxl) = cv2.minMaxLoc(result)
    (startX, startY) = maxl
    endX = startX + img_temp.shape[1]
    endY = startY + img_temp.shape[0]

    cv2.rectangle(img, (startX, startY), (endX, endY), (255,0,0),3)
    cv2.imwrite('data/result/tm/temp/img'+str(i)+'.jpg', img)

if __name__ == '__main__':
    imgs = os.listdir('data/orig/images')
    temps = os.listdir('data/orig/templates')
    
    for i in range(len(imgs)):
        img = cv2.imread('data/orig/images/'+imgs[i])
        img_temp = cv2.imread('data/orig/images/'+temps[i])
        kp_detection(img, img_temp,i)
        temp_matching(img, img_temp,i)