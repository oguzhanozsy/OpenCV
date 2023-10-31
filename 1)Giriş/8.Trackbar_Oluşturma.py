import cv2
import numpy as np

def nothing(x): # boş bir değer alan fonksiyondur,kullanıldığı yerdeki parametrenin boş kalmaması içindir yani bir işlevi yoktur...
    pass


# Siyah ekran oluştur ve bir de pencere

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

# Renk değşim çubukları(trackbar) oluştur

cv2.createTrackbar("R","image",0,255,nothing) #trackbarı oluşturur.Aldığı parametreler sırasıyla(ismi/hangi pencerede bulunacağı/başlangıç değeri/bitiş değeri/başka bir parametre alıyor ama bu trackbarda ihtiyacımız olmadığı için boş bir fonksiyon atadık)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
cv2.createTrackbar("ON-OFF","image",0,1,nothing)

while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R','image')  # Harfi R olan image üzerindeki trackbarın konumunu al ve r değişkenine ata demektir...
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos('ON-OFF','image')
    if s == 0:  # anahtar kapalıysa
        img[:] = 0  # renk değerlerini gösterme
    else:  # anahtar açıksa
        img[:] = [r, g, b]  # renk değerlerini göster




cv2.destroyAllWindows()