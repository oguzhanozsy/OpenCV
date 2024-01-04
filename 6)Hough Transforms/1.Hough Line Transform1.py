import cv2
import numpy as np

img = cv2.imread("lines.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY) # resmin gri tona dönüştürür...

edges = cv2.Canny(gray,75,150) # resmin köşelerini edges değişkeninde tutar.İçeriği sırala(resim/min değer/max değer)...

# cv2.HoughLines() Alttaki satırdakini kullanıyoruz çünkü bu GPU yu daha çok yoruyor...
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200) # Çizgileri Tespit eder ve lines değişkemine atar. İçeriği sırayla(köşeleri tespit edilmiş resim/row/teta/thresh miktarı/çizgiler arası boşluğu doldurma miktarı)...

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()