import cv2

img = cv2.imread("contour1.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY) # resmi griye çevirir...

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # görüntünün piksel değerlerini ikiye ayırır(siyah ve beyaz) ve resimdeki gürültüleri azaltır...

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# kontür koordinatlarını bulur.İçeriği sırayla(threslenmiş resim,diğer iki argüman kontür bulma işlemini daha doğru yapıyor default fonksiyonlardır)...

cv2.drawContours(img,contours,-1,(0,0,255),3) # resmin kenarlarına çizgi çizmeyi sağlar.İçeriği sırayla(kenarları çizilecek resim/çizgilerin koordinatları/-1/çizgi rengi/çizgi kalınlığı)...

cv2.imshow("contour",img)

cv2.waitKey(0)
cv2.destroyAllWindows()