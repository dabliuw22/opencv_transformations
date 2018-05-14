# -*- coding: utf-8 -*-
import cv2
import numpy as np

#Cargar imagen en escala de grises
image = cv2.imread('/home/will/Imágenes/morpho.png', 0)
cv2.imshow('Original', image)
cv2.waitKey(0)

# Crear kernel 5x5
kernel = np.ones((5, 5), np.uint8)

# Aplicar Dilatación
dilation_image = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation_image)
cv2.waitKey(0)

cv2.destroyAllWindows()