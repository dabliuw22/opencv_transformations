# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/venon.jpg')

# Re-sizing: reduciendo a la mitad el tamaño (Pyramids)
image_smaller = cv2.pyrDown(image)

# Re-sizing: aumentando la mitad del tamaño (Pyramids)
image_larger = cv2.pyrUp(image)


cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)


cv2.namedWindow('Smaller', cv2.WINDOW_NORMAL)
cv2.imshow('Smaller', image_smaller)
cv2.namedWindow('Larger', cv2.WINDOW_NORMAL)
cv2.imshow('Larger', image_larger)

cv2.waitKey(0)
cv2.destroyAllWindows()
