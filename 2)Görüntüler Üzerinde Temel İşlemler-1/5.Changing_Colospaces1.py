import cv2

img = cv2.imread("araba.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # resmin renginin değiştirir ve bunu bir değişkene atar.Aldığı parametreler sırayla(rengi değişecek resim/normal renginden dönüşeceği renk belirtilir) #bgr(orjinal rengi) -> gray(gri) yapmak için cv2.COLOR_BGR2GRAY kullanılır...

cv2.imshow("Img",img) # orjinal resmi gösterir...
cv2.imshow("Gray",gray) # rengi değişmiş resmi gösterir...

cv2.waitKey(0)
cv2.destroyAllWindows()