import cv2


# cv2 dan foydalangan holda rasm hajmini o'zgartiris va kesish

img = cv2.imread("Resources/gentra.jpg") # Rasmni dasturga yuklaymiz

# Rasmning haqiqiy o'lchamini bilish uchun pastdagi funksiya ishlatilinadi 
#print(img.shape)

imgResize = cv2.resize(img,(1000,500))  # Rasm o'lchamini o'zgartirish

imgCropped = img[46:300,352:640] # Rasmdan qirqib olish

cv2.imshow("Image",img)                     #
cv2.imshow("Image Resize",imgResize)        #   Tayyorlangan rasmlarni ekranga chiqarish
cv2.imshow("Image Cropped",imgCropped)      #

cv2.waitKey(0) # Dastur o'chib qolmasligi uchun funksiya