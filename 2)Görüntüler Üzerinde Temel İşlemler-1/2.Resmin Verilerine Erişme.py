import cv2
import numpy as np

img = cv2.imread('helikopter.jpg')

print(img.shape) # sırayla ilk ikisi resmin boyutlarını ve son veride nasıl bi kanaldan oluştuğunu söyler mesela 3 ise rgb den oluşmuş demektir...
print(img.size) #toplam pixel sayısını verir...