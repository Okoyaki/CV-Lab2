import cv2


def temp_matching(img, img_temp,i):
    result = cv2.matchTemplate(img,img_temp, cv2.TM_CCOEFF_NORMED)

    (minv, maxv, minl, maxl) = cv2.minMaxLoc(result)
    (startX, startY) = maxl
    endX = startX + img_temp.shape[1]
    endY = startY + img_temp.shape[0]

    cv2.rectangle(img, (startX, startY), (endX, endY), (255,0,0),3)
    cv2.imwrite('data/result/tm/temp/img'+str(i)+'.jpg', img)

# imgs = os.listdir('data/orig/images')
# temps = os.listdir('data/orig/templates')
img_temp = cv2.imread('data/orig/templates/img1.jpg')
img = cv2.imread('data/orig/images/img1.jpg')
# kp_detection(img, img_temp,0)
temp_matching(img, img_temp,0)