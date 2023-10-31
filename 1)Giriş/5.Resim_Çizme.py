import cv2
import numpy as np # matematiksel ifadeleri içeren kütüphanedir...

img = np.zeros((512,512,3),np.uint8) # sıfırlardan oluşan bir matris oluşturur.Parantez içindeki ilk iki sayı ekranın boyutlarını oluşturur,üçüncü veri ise rgb kanallarının sayısını oluşturur.Parantezin dışındaki ifade de int tipine dönüştürür...
cv2.line(img,(100,100),(360,480),(100,100,0),5) # Ekrana çizgi çizer. Sırayla aldığı parametreler(neyin üzerine çizileceği/başlangıç noktası/bitiş noktası/renk/kalınlık)...

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
