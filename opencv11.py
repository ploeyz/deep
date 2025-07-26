import cv2

face = cv2.CascadeClassifier('photo/haarcascade_frontalface_default.xml')
print(face)

img = cv2.imread('photo/Chelsea.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

counter = 1


for (x, y, w, h) in faces:
    face_img = img[y:y+h, x:x+w]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(f'photo/face/face_{counter}.jpg', face_img)
    counter += 1

cv2.imshow('Detected Faces', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
