import cv2

img = cv2.imread('photo/Chelsea.jpg')

resize = cv2.resize(img, (500, 300))

cv2.imshow('Resize Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()