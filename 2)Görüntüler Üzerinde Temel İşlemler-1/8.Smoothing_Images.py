import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter,(5,5)) # resmin yumuşamasını sağlar.Parametreler her zaman pozitif tek sayıları alır ve yumuşaklık değeridir...
blur_g = cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT) # Yine resmin yumuşamasını sağlar.Border default sınır çizgileri aynı kalsın demek çokda önemli bişi değil...
blur_m = cv2.medianBlur(img_median,5) # gürültülü resimlerin gürültüsünü azaltır. Yine pozitif tek sayıları alır.
blur_b = cv2.bilateralFilter(img_bilateral,9,75,75) # resmi pürüzleştirir.Parametreler pixel değerleridir...

cv2.imshow("original",img_filter)
cv2.imshow("blur",blur)
cv2.imshow("blur_g",blur_g)
cv2.imshow("blur_m",blur_m)
cv2.imshow("bilateral",img_bilateral)
cv2.imshow("blur_b",blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
