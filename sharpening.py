# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/ubuntu.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Crear un kernel
kernel = np.array([[-1, -1, -1],
				   [-1, 9, -1],
				   [-1, -1, -1]])

# Aplicando convolución para 
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow('Nitidez', sharpened)
cv2.waitKey(0)

cv2.destroyAllWindows()