# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/cebra.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Aplicando Sobel horizontal y vertical
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 5)

cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)

sobel_or = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('Sobel OR', sobel_or)
cv2.waitKey(0)

# Aplicando Laplacian para detección de bordes
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)

# Aplicando Canny para detección de bordes
canny = cv2.Canny(image, 20, 170)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()