# -*- coding: utf-8 -*-
import numpy as np
import cv2

image = cv2.imread("/home/will/Imágenes/140062-1.png")

# Obtenemos filas y columnas (alto y ancho)
height, width = image.shape[:2]

h, w = height/4, width/4

'''
T = |1 0 Tx|
	|0 1 Ty|
'''
cv2.namedWindow('Mover', cv2.WINDOW_NORMAL)
# Creamos una matriz de float
t = np.float32([[1, 0, w], [0, 1, h]])

# Trasladamos la imagen y la obtenemos
image_translation = cv2.warpAffine(image, t, (width, height))
cv2.imshow('Mover', image_translation)

cv2.waitKey()
cv2.destroyAllWindows()