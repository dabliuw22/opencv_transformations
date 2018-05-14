# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/ubuntu.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Kernel promedio de 3x3
# La suma de todos sus valores debe ser 1
# Todos los valores deben ser iguales.
kernel3x3 = np.ones((3, 3), np.float32)/9

# Difuminado (Filtro Medio) aplicando convolución 2D.
blurred = cv2.filter2D(image, -1, kernel3x3)
cv2.imshow('Blurring 3x3', blurred)
cv2.waitKey(0)

# Kernel promedio de 7x7
# La suma de todos sus valores debe ser 1
# Todos los valores deben ser iguales.
kernel7x7 = np.ones((7, 7), np.float32)/49

# Difuminado (Filtro Medio) aplicando convolución 2D.
blurred_two = cv2.filter2D(image, -1, kernel7x7)
cv2.imshow('Blurring 7x7', blurred_two)
cv2.waitKey(0)

cv2.destroyAllWindows()