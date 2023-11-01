import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Trackbar") # pencere oluşturur...
cv2.resizeWindow("Trackbar",500,250) # pencereyi boyutlandırır...

cv2.createTrackbar("Lower-H","Trackbar",0,180,nothing) # trackbarları oluşturur.Sırayla parametreler(Tracbarın ismi/bulunacağı pencerenin ismi/başlangıç değeri/bitiş değeri/boş parametre)
cv2.createTrackbar("Lower-S","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower-V","Trackbar",0,255,nothing)

cv2.createTrackbar("Upper-H","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper-S","Trackbar",0,255,nothing)
cv2.createTrackbar("Upper-V","Trackbar",0,255,nothing)

cv2.setTrackbarPos("Upper-H","Trackbar",180) #trackbarın üzerindeki kızağı oluşturur. Aldığı parametreler sırayla(Max değerli Tracbarın ismi/tracbarın hangi pencerede olacağı/kızağın maks değeri)
cv2.setTrackbarPos("Upper-S","Trackbar",255)
cv2.setTrackbarPos("Upper-V","Trackbar",255)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1) # aldığı framleri y eksenine göre ters çevirir yani gerçekte sağ elimizi kaldırırsak webcamde de sağ elin kalkmasını sağlar...
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Lower-H","Trackbar")
    ls = cv2.getTrackbarPos("Lower-S", "Trackbar")
    lv = cv2.getTrackbarPos("Lower-V", "Trackbar")

    uh = cv2.getTrackbarPos("Upper-H", "Trackbar")
    us = cv2.getTrackbarPos("Upper-S", "Trackbar")
    uv = cv2.getTrackbarPos("Upper-V", "Trackbar")

    lower_color = np.array([lh,ls,lv]) # mask için lower değerleri bir değişkene atıyoruz...
    upper_color = np.array([uh, us, uv]) # mask için upper değerleri bir değişkene atıyoruz...

    mask = cv2.inRange(hsv,lower_color,upper_color) # masklama işlemi

    cv2.imshow("original",frame) # orjinal videoyu gösterir...
    cv2.imshow("mask",mask) # mask işlemi yapılan videoyu gösterir...

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()  # videoyu serbest bırakır...
cv2.destroyAllWindows()