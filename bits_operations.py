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

and_image = cv2.bitwise_and(image, image_two)
cv2.imshow('And', and_image)
cv2.waitKey(0)

or_image = cv2.bitwise_or(image, image_two)
cv2.imshow('Or', or_image)
cv2.waitKey(0)

xor_image = cv2.bitwise_xor(image, image_two)
cv2.imshow('Xor', xor_image)
cv2.waitKey(0)

not_image = cv2.bitwise_not(image_two)
cv2.imshow('Not', not_image)
cv2.waitKey(0)

cv2.destroyAllWindows()