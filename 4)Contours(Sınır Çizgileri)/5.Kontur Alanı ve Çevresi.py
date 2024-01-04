import cv2

img = cv2.imread("contour.png") # resmi okur...

gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY) # resmi gri hale çevirir...
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # resmi treshler...
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt) # üçgenin alanını bulur...
print(area)
M = cv2.moments(cnt)  # resimle ilgili bilgileri sözlük yapısında tutar...
print(M["m00"])

perimeter = cv2.arcLength(cnt,True) # resmin çevresini bulur.İçeriği(resim/resmin kapalı olup olmadığı)
print(perimeter)


cv2.waitKey(0)
cv2.destroyAllWindows()

