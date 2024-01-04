import cv2
import numpy as np

img = cv2.imread("map.jpg") # resmi okur...

gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY) # resmi gri tona çevirir...
blur = cv2.blur(gray,(3,3)) # resmi bulurlar...
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY) # resmi thresler...

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # contourların koordinatlarını bulur...

hull = [] # boş bir dizi atadık...

for i in range(len(contours)): # 0 dan contourun değerinin sonuna kadar döndürür...
    hull.append(cv2.convexHull(contours[i],False)) # bu değerleri boş dizeye aktarır...

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)  # siyah ekran oluşturur...

for i in range(len(contours)): # 0 dan contourun değerinin sonuna kadar döndürür...
    cv2.drawContours(bg,contours,i,(255,0,0),3,8,hierarchy) # çizgi çizer...
    cv2.drawContours(bg,hull,i,(0,255,0),1,8) # çizgi çizer...

cv2.imshow("Image",bg)


cv2.waitKey(0)
cv2.destroyAllWindows()