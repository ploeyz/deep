import cv2

img = cv2.imread('photo/chelsea.jpg')

cv2.line(img, (0, 0), (150, 150), (250, 255, 50), 6)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()