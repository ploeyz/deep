import cv2
# read image from file
img = cv2.imread('photo/Chelsea.jpg')
cv2.imshow('PHOTO', img)

cv2.waitKey(0)
cv2.destroyAllWindows()