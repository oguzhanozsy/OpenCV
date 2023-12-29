import cv2

# cv2.Canny(input,minThreshold,maxThreshold) resimdeki kenarları bulmaya yarayan fonksiyondur.İçeriği sırasıyla(Kenarları tespit edilecek resim,min traşlama değeri,max traşlama değeri)

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read() # tüm resim piksellerini okur...
    frame = cv2.flip(frame,1) # görüntüyü takla attırır.İçeriği sırayla(piksel(kare)/y eksenine göre görüntünün tersini alır(bunu yapmasının sebebi gerçkete sağ elimizi kaldırınca ekranda da sağ tarafın kalktığını görmek))...

    edges = cv2.Canny(frame,100,200) # resimdeki kenarları edges değişkenine atar...

    cv2.imshow("Frame",frame) # orjinal halini gösterir...
    cv2.imshow("Edges",edges) # kenarların bulunduğu halini gösterir...

    if cv2.waitKey(5) & 0xFF == ord("q"): # programdan çıkış bloğudur...
        break

cap.release()
cv2.destroyAllWindows()

