import cv2
import numpy as np

img = cv2.imread("helikopter2.jpg",0)

kernel = np.ones((5,5),np.uint8) # çekirdek yapısıdır ve 1 sayısı ile resmi bozmaya yarar.İçeriği Sırayla(Matris boyutu/int tipi olduğunu belirtir)

"erosion"
erosion = cv2.erode(img,kernel,iterations = 1) # sırayla(orjinal resim/çekirdek yapısı/işlemin kaç defa tekrar edeceği)...

"dilation(kalınlaştırma)"
dilation = cv2.dilate(img,kernel,iterations = 5) # sırayla(orjinal resim/çekirdek yapısı/işlemin kaç defa tekrar edeceği)...

"opening(resimdeki gürültüleri silme)"
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) # sırayla(orjinal resim/hazır fonksiyon/çekirdek yapısı)...

"closing(resimdeki şekillerin içindeki gürültüleri silme)"
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) # sırayla(orjinal resim/hazır fonksiyon/çekirdek yapısı)...

"gradient(resimdeki şeklin dış hattını beyaz ile çizer içindeki kısmı siyahla çizer)"
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) # sırayla(orjinal resim/hazır fonksiyon/çekirdek yapısı)...

"tophat(resimdeki şeklin bazı kısımlarını karartır)"
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel) # sırayla(orjinal resim/hazır fonksiyon/çekirdek yapısı)...

"blackhat(resimdeki şeklin bazı kısımlarını karartır)"
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel) # sırayla(orjinal resim/hazır fonksiyon/çekirdek yapısı)...

cv2.imshow("img",img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
