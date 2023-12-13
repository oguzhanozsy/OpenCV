import cv2
import numpy as np

img = cv2.imread("helikopter.jpg")

row,col,kanal = img.shape # resmin boyutlarını ve kanal değerini sırayla değişkenlere atar...

M = cv2.getRotationMatrix2D((col/2,row/2),90,1) # 2 boyutta yön değiştirmeyi sğlayan fonksiyondur. İçeriği sırayla((istenilen satır ve sütun boyutu),döndürme açısı,ölçek)...

dst = cv2.warpAffine(img,M,(col,row)) # resmi döndürüp dst değişkenine atar. Fonksiyon sırayla (döndürülecek resmi,döndürme değerlerini,açılacak pencerenin boyutları)ni alır...

cv2.imshow("dst",dst) # döndürülmüş resmi ekranda gösterir...

cv2.waitKey(0)
cv2.destroyAllWindows()