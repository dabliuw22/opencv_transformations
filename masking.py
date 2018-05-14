# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = np.zeros((300, 300), np.uint8)

# Agregando mascara rectangular a la imagen
cv2.rectangle(image, (50, 50), (250, 250), (255, 0, 0),-2)

cv2.namedWindow('Mascara Rectangular', cv2.WINDOW_NORMAL)
cv2.imshow('Mascara Rectangular', image)
cv2.waitKey(0)


image_two = np.zeros((300, 300), np.uint8)

# Agregando mascara eliptica a la imagen
cv2.ellipse(image_two, (150, 150), (150, 150), 30, 0, 180, (255, 0, 0),-1)

cv2.namedWindow('Mascara Eliptica', cv2.WINDOW_NORMAL)
cv2.imshow('Mascara Eliptica', image_two)
cv2.waitKey(0)
cv2.destroyAllWindows()