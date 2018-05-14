# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/venon.jpg')
height, width = image.shape[:2]

m = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotated_image = cv2.warpAffine(image, m, (width, height))

other_rotated_image = cv2.transpose(image)

cv2.namedWindow('Imagen rotada', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen rotada', rotated_image)

cv2.namedWindow('Otra imagen rotada', cv2.WINDOW_NORMAL)
cv2.imshow('Otra imagen rotada', other_rotated_image)

cv2.waitKey()
cv2.destroyAllWindows()