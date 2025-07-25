import cv2

img = cv2.imread('photo/chelsea.jpg')

cv2.circle(img, (250, 250), 70, (255, 0, 50), -1)
cv2.circle(img, (100, 100), 70, (255, 0, 50), 6)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()