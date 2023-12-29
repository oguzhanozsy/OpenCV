import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
->Histogram kullanarak resimler üzerinde çözümlemeler yapabiliriz...
->Histogramı grafik olarak düşünebiliriz.Bu grafik resmin değer yoğunluklarıyla ilgili bilgiler verir...
->Bir resmin histogramına baktığımızda o resmin aydınlık noktalarını,karanlık noktalarını ve constrat değerleriyle ilgili çıkarımlarda bulunabiliriz...
"""
####################################
"""
img = np.zeros((500,500),np.uint8) + 50 # 500'e 500'lük bir siyah(tabi +50 yaparsak rengi grileşir tma siyah olmaz) ekran oluşturur...
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)  # beyaz bir dikdörtgen çizer...
cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1) # beyaz bir dikdörtgen çizer...

cv2.imshow("img",img)

plt.hist(img.ravel(),256,[0,256]) #histogram çizmeye yarayan fonksiyondur.İçeriği sırayla(resmin tüm piksellerini tek bir satıra döken fonksiyon(histogram çizmek için bu gereklidir)/Ölçmek istediğiniz yoğunluk değerleri aralığıdır. Normalde [0,256]'dır, yani tüm yoğunluk değerleri/yoğunluk değer aralığı)
plt.show()
"""
####################################

img = cv2.imread("smile.jpg")
b,g,r = cv2.split(img)

cv2.imshow("img",img)

plt.hist(b.ravel(),256,[0,256]) # mavi rengi için histogram oluşturur...
plt.hist(g.ravel(),256,[0,256]) # yeşil rengi için histogram oluşturur...
plt.hist(r.ravel(),256,[0,256]) # kırmızı rengi için histogram oluşturur...
plt.show()

#####################################

cv2.waitKey(0)
cv2.destroyAllWindows()
