# import cv2
# import numpy as np

# img = cv2.imread('data/orig/images/img1.jpg')
# img_temp = cv2.imread('data/orig/templates/img1.jpg')
# img_temp2 = cv2.imread('data/orig/templates_add/img1.jpg')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_temp = cv2.cvtColor(img_temp, cv2.COLOR_BGR2RGB)
# img_temp2 = cv2.cvtColor(img_temp2, cv2.COLOR_BGR2RGB)

import cv2
import numpy as np

def detect_objects(reference_image_path, input_image_path):
    reference_image_orig = cv2.imread('data/orig/templates/img1.jpg')
    input_image_orig = cv2.imread('data/orig/images/img1.jpg')

    reference_image = cv2.cvtColor(reference_image_orig, cv2.COLOR_RGB2GRAY)
    input_image = cv2.cvtColor(input_image_orig, cv2.COLOR_RGB2GRAY)

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

        cv2.rectangle(input_image_orig, (x_min, y_min), (x_max, y_max), (255, 0, 0), 3)


    # Вывод результата
    cv2.imshow("Matches and Object Detection", input_image_orig)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    reference_image_path = "reference.jpg"  # Путь к эталонному изображению
    input_image_path = "input.jpg"          # Путь к изображению для анализа

    detect_objects(reference_image_path, input_image_path)