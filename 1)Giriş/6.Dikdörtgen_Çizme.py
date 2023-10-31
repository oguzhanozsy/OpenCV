import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img,(0,0),(100,100),(100,123,213),3) # dikdörtgen çizmeyi sağlar.Aldığı parametreler sırayla(neyin üzerine çizileceği/başlangıç koordinatı/bitiş koordinatı/renk/kalınlık)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

