import cv2

img = cv2.imread("contour1.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY) # resmi griye çevirir...

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # görüntünün piksel değerlerini ikiye ayırır(siyah ve beyaz) ve resimdeki gürültüleri azaltır...

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# kontür koordinatlarını bulur.İçeriği sırayla(threslenmiş resim,diğer iki argüman kontür bulma işlemini daha doğru yapıyor default fonksiyonlardır)...

print(contours)