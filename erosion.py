# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/morpho.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Crear kernel 5x5
kernel = np.ones((5, 5), np.uint8)

# Aplicar erosión
erode_image = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erotion', erode_image)
cv2.waitKey(0)

cv2.destroyAllWindows()