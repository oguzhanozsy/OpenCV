import cv2
import numpy as np

vid = cv2.VideoCapture("traffic.avi")

while 1:
    _,frame = vid.read() # videoyu kare kare frame değişkenine çeker(ilk parametre doğru oynatılıp oynatılmadığını kontrol ediyo,şuan ihtiyacımız olmadığı için '_' kullanarak boş bıraktık)...
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # videoyu hsv formatına dönüştürür.Sırayla aldığı parametreler(dönüştürülecek video/neye dönüşeceği)...

    #HSV'nin açılımı:(Hue: renkleri temsil eder// Saturation: Renklerin yoğunluğunu temsil eder // Value: aydınlık karanlık noktaları temsil eder)...

    lower_yellow = np.array([18,94,150]) # en düşük sarı renk kodunu bir değişkene atadık bu değerleri internetten bulabilirsiniz...
    upper_yellow = np.array([48,255,255]) # en yüksek sarı renk kodunu bir değişkene atadık bu değerleri internetten bulabilirsiniz...

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow) # mask işlemi yapar yani siyah ekranda bulmak istediğimiz rengi beyaz olarak gösterir.Sırayla aldığı parametreler:(HSV arayüzüne çevirdiğimiz video/aradığımız rengin en düşük değeri/aradığımız rengin en yüksek değeri)...

    cv2.imshow("Frame",frame) # orjinal videoyu gösterir...
    cv2.imshow("MASK",mask) # maskladığımız videoyu gösterir

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()