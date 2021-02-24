import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('result.png', cv2.IMREAD_COLOR)

cv2.imshow('original Image', img)
#cv2.waitKey(0) #이미지를 읽고 꺼지지 않게
cv2.imwrite('./test_image/result.png', img)



img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image',img_gray)
#cv2.waitKey(0)
cv2.imwrite('./test_image/result_Gray.png', img_gray)
# cv2.resize(image, dsize, fx, fy, interpolation)  ; dsize = Manual Size, fx = 가로비율 ,fy = 세로비율, interpolation = 보간법(사이즈 변환시 픽셀사이 값 조절하는법)  보통 사이즈를 크게할땐 INTER_CUBIC, 작게할떈 INTER_AREA

img_expand = cv2.resize(img, None, fx = 2.0, fy = 2.0, interpolation = cv2.INTER_CUBIC)
cv2.imshow('expand',img_expand)
#cv2.waitKey(0)
cv2.imwrite('./test_image/expand.png', img_expand)

img_shrink = cv2.resize(img, None, fx = 0.2, fy = 0.5, interpolation = cv2.INTER_AREA)
cv2.imshow('shrink', img_shrink)
#cv2.waitKey(0)
cv2.imwrite('./test_image/shrink.png', img_shrink)


#cv2.warpAffine(image, M, dsize) 이미지 위치를 변경, M 변환행렬 - 이미지 참고, dsize = manual Size

height, width = img.shape[:2] #행과 열 정보만 가져오기
M = np.float32([[1, 0, 50], [0, 1, 10]]) #오른쪽으로 50만큼 아래로 10만큼 이동하는 변환행렬
img_move = cv2.warpAffine(img, M, (width, height))
cv2.imshow('move', img_move)
cv2.imwrite('./test_image/move.png', img_move)
cv2.waitKey(0)

cv2.destroyAllWindows()
