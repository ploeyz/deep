import cv2

img = cv2.imread('photo/chelsea.jpg')

cv2.putText(img, 'OpenCV', (180, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 182, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()