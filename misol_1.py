import cv2
# Rasmlar bilan ishlash uchun cv2 kutubxonasini chaqirib olamiz
img = cv2.imread("res/lena.png")
# Ochmoqchi bo'lgan rasmimizni mnzilini ko'rsatamiz
cv2.imshow("Lena", img)
cv2.waitKey(0)

# Dastur ishlab turishi uchun waitKey(0) dan foydalanamiz