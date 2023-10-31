import cv2
import numpy as np

img = cv2.imread("helikopter.jpg")

# ROI --> region of image (412 640)(resmin boyutu) dikey(256 156)(keseceğimiz kısmın dikey koordinatları) yatay (0,80)(keseceğimiz kısmın yatay koordinatları)

kuyruk = img[156:256,0:80] #keseceğimiz kısmın koordinatlarını kuyruk değişkenine atadık...
img[0:100,300:380] = kuyruk #kestiğimiz kısmın yeni konumuna, kestiğimiz kısmın koordinatlarını atadık...

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()