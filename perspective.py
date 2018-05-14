# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/morpho.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Especificamos coordenadas de zona
points_a = np.float32([[320, 15],
					   [700, 215],
					   [85, 610],
					   [530, 780]])
# Especificamos coordenadas de imagen de salida
points_b = np.float32([[0, 0],
					   [420, 0],
					   [0, 594],
					   [420, 594]])
# Obtención de matriz de transformación
m = cv2.getPerspectiveTransform(points_a, points_b)
# Aplicar perspectiva
warped = cv2.warpPerspective(image, m, (420, 594))
cv2.imshow('Perspective', warped)
cv2.waitKey(0)

# Especificamos coordenadas de zona
points_c = np.float32([[320, 15],
					   [700, 215],
					   [85, 610]])
# Especificamos coordenadas de imagen de salida
points_d = np.float32([[0, 0],
					   [420, 0],
					   [0, 594]])
# Obteniendo matriz de transformación de perspectiva
n = cv2.getAffineTransform(points_c, points_d)
affine = cv2.warpAffine(image, n, (420, 594))
cv2.imshow('Perspective Afine', affine)
cv2.waitKey(0)

cv2.destroyAllWindows()