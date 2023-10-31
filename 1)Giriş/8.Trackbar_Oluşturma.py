import cv2
import numpy as np

# Siyah ekran oluştur ve bir de pencere

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

