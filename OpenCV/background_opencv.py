import cv2
import numpy as np


def change_color(x): # 매개변수x는 getTrackbarPos로 전달될 Trackbar위치 값 의미함
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")
    image[:] = [b,g,r]
    cv2.imshow("Image", image)

image = np.zeros((600, 400, 3), np.uint8) # RGB를 위한 numpy객체 생성
cv2.namedWindow("Image")

cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)
