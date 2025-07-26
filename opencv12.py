import cv2

video_path = 'video/ronaldo.mp4'

cap = cv2.VideoCapture(video_path)

while True:
    success, frame = cap.read()
    if not success:
        print("read video failed")
        break
    
    cv2.imshow("Video Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()