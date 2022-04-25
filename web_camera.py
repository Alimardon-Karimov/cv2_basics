import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)   # Agar VideoCapture ga manzil o'rniga '0' qo'ysnagiz 
                            # u web kamerani ishga tushiradi
cap.set(3, frameWidth)      # set(3, tasvirning_eni)
cap.set(4, frameHeight)     # set(4, tasvirning_bo'yi)
cap.set(10, 150)            # set(10, tasvirning yorg'ligi)

while True:
    success, img = cap.read() # success bizga video xatosiz yuklanganini bildiradi. Qiymati True yoki False
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break