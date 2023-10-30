import cv2

yVid = cv2.VideoCapture('sokak.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cikti = cv2.VideoWriter('sokakIsiklari.mp4',fourcc,20.0,(640,480))


while(True):
    deger,kare = yVid.read()
    if deger == True:
        cikti.write(kare)
        cv2.imshow('Sehir Isiklari',kare)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            break

yVid.release()
cikti.release()
cv2.destroyAllWindows()