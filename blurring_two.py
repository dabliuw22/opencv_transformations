# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/ubuntu.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Filtro promedio
blur = cv2.blur(image, (3, 3))
cv2.imshow('Averaging', blur)
cv2.waitKey(0)

# Filtro Gaussiano
gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian', blur)
cv2.waitKey(0)

#Filtro de Mediana (diferente de filtro Media)
median = cv2.medianBlur(image, 5)
cv2.imshow('Median', median)
cv2.waitKey(0)

# Filtro Bilateral
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()