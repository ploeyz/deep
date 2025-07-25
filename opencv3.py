import cv2 

img = cv2.imread('photo/Chelsea.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)

cv2.imshow('PHOTO', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()