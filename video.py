import cv2

cap = cv2.VideoCapture("Resources/test_video.mp4")      # VideoCapture yordamia videoni yuklaymiz

while True:
    success, img = cap.read()               # Videoni ekranga chiqaramiz
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # Agar klaviaturada 'q' bosilsa video to'xtatiladi 
        break