import cv2

img = cv2.imread('helikopter.jpg',0)
cv2.imshow('RESIM',img)

dugme = cv2.waitKey(0)

if dugme == 27: # 27 sayısı 'esc' yi temsil eder...
    cv2.destroyAllWindows()
else:
    cv2.imwrite('gri_helikopter.jpg',img) # resmi kaydetmeye yarar. İlk parametre resmin yeni ismidir, ikinci parametre kaydedilecek resmin değişkenini alır...