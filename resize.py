# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/ubuntu.png')

# Re-sizing con interpolación lineal
image_scaled = cv2.resize(image, None, fx = 0.5, fy = 0.75)

cv2.namedWindow('Scaling - Linear Interpolation', cv2.WINDOW_NORMAL)
cv2.imshow('Scaling - Linear Interpolation', image_scaled)
cv2.waitKey()

# Re-sizing con interpolación Cubica
image_scaled_two = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

cv2.namedWindow('Scaling - Cubic Interpolation', cv2.WINDOW_NORMAL)
cv2.imshow('Scaling - Cubic Interpolation', image_scaled_two)
cv2.waitKey()

# Re-sizing con interpolación de Area con dimensiones (900, 400)
image_scaled_three = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)

cv2.namedWindow('Scaling - Area Interpolation', cv2.WINDOW_NORMAL)
cv2.imshow('Scaling - Area Interpolation', image_scaled_three)
cv2.waitKey()

cv2.destroyAllWindows()