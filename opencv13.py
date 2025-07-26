import cv2

video_path = 'video/ronaldo.mp4'


face = cv2.CascadeClassifier('photo/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(video_path)

while True:
    success, frame = cap.read()
    if not success:
        print("read video failed")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        #face_img = img[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Video Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()