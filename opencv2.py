import cv2

img = cv2.imread('photo/chelsea.jpg')
cv2.imwrite('photo/newchelsea.jpg', img)
print("Image saved successfully.")