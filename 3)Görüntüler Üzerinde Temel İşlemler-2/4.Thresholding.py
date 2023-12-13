import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Thresholding: resimleri gruplandırma treshleme yöntemidir, bu yöntemle resmin çeşitli özellikleri, ayrıntıları ortaya çıkar...
"""


img = cv2.imread("helikopter2.jpg",0) # thresholding yapmak için resmimiz siyah-beyaz(gri) tonda olması gerekir o yüzden sıfır yazdık...

ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY) # yeni resmi iki değişkende tutarız ret dönüş değerini tutar, th1 de yeni resmi tutar.Fonksiyonun içi sırayla(thresh edilecek resim/min thresh değeri/max thresh değeri/hazır fonksiyon)....
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,2) # başka bir thresh yöntemidir.Fonksiyonun içi sırayla(thresh edilecek resim/max thresh değeri/hazır fonksiyon/hazır fonksiyon/çizgi kalınlığı(iki ile bölümünden kalanı 1 olan sayılar olmalı)/sabit(cızırtıları yok eder))...
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2) # başka bir thresh yöntemidir.Fonksiyonun içi sırayla(thresh edilecek resim/max thresh değeri/hazır fonksiyon/hazır fonksiyon/çizgi kalınlığı(iki ile bölümünden kalanı 1 olan sayılar olmalı)/sabit(cızırtıları yok eder))

cv2.imshow("img-th1",th1)
cv2.imshow("img-th2",th2)
cv2.imshow("img-th3",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
