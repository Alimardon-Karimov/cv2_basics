import cv2   # Rasmlar bilan ishlash uchun cv2 kubxonasini chaqirib olamiz

img = cv2.imread("resources/gentra.jpg")  # imread() orqali rasmni dasturga yuklaymiz
cv2.imshow("Gentra", img)  # yuklangan rasmni ekranga chiqarami

cv2.waitKey(0)     # Dastur o'chib qolmasligi uchun waitKey(0) dan foydalanamiz


