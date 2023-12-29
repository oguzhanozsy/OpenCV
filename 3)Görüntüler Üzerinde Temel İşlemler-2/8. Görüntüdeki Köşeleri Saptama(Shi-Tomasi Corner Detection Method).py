import cv2
import numpy as np

img1 = cv2.imread("text.png")
img2 = cv2.imread("contour.png")

gray = cv2.cvtColor(img1,cv2.COLOR_BGRA2GRAY) # resmi gri hale getirir...
gray = np.float32(gray) # aşağıdaki fonksiyonda gray değişkenini doğrudan kullanamadığımız için float32 tipine dönüştürdük...

corners = cv2.goodFeaturesToTrack(gray,50,0.01,10) # köşeleri bulan fonksiyondur. İçeriği sırasıyla(köşeleri bulunacak gri formattaki resim/toplam bulmasını istediğimiz köşe sayısı/kalite değeri/köşeler arası minimum mesafe)

corners = np.int0(corners) # çemberler çizerken float kullanamadığımız için int tipine değiştiriyoruz...

for corner in corners:
    x,y = corner.ravel() # x,y leri tek bir satıra aktarır...
    cv2.circle(img1,(x,y),3,(0,0,255),-1) # çember çizer...

cv2.imshow("corner",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
