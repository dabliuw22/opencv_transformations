# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/venon.jpg')
height, width = image.shape[:2]

# Puntos x, y de comienzo recorte
start_row, start_col = int(height*.25), int(width*.25)

# Puntos x, y de fin de recorte
end_row, end_col = int(height*.75), int(width*.75)

cropped_image = image[start_row:end_row, start_col:end_col]

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)
cv2.waitKey()

cv2.namedWindow('Recortada', cv2.WINDOW_NORMAL)
cv2.imshow('Recortada', cropped_image)
cv2.waitKey()

cv2.destroyAllWindows()