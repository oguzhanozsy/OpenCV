import cv2

yVid = cv2.VideoCapture('sokak.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID') #fourcc kodları,video kaydetmele alakalı kodlardır...
cikti = cv2.VideoWriter('sokakIsiklari.mp4',fourcc,20.0,(640,480)) #videonun kaydedilmesini sağlar,ilk parametreye kaydedilecek videonun adı yazılır,ikinciye fourcc kodları,üçüncüye saniye başına görmek istediğimiz kare sayısıdır(fps),dördüncü ise videonun görüntülenme biçimi yani boyutları girilir...


while(True):
    deger,kare = yVid.read()
    if deger == True:
        cikti.write(kare) # her resim karesi doğru çekildiyse onları yaz demektir...
        cv2.imshow('Sehir Isiklari',kare)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            break

yVid.release()
cikti.release() #çıktıları serbest bırakır...
cv2.destroyAllWindows()