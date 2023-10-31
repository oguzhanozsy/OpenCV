import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.circle(img,(100,100),60,(255,0,0),) # Çember çizmeyi sağlar.Aldığı parametreler sırayla(neyin üzerine çizileceği/merkez koordinatları/yarıçapı/renk/içinin dolu olup olmaması(-1 olursa dolu olur,hiçbir şey yazmazsak boş olur))...

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()