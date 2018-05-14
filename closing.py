# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/morpho.png')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Kernel
kernel = np.ones((5, 5), np.uint8)

# Aplicando cierre
opening_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Opening', opening_image)
cv2.waitKey(0)

cv2.destroyAllWindows()