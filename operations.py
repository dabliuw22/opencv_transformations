# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('/home/will/Imágenes/ubuntu.png')

# Creamos una matriz de 1 y l multiplicamos por un escalar
# Con la cual operaremos para aumentar y/o decrementar el brillo
m = np.ones(image.shape, dtype = 'uint8')*75

# Aumentar brillo
added = cv2.add(image, m)
cv2.imshow("Added", added)

# Disminuir brillo
subtract = cv2.subtract(image, m)
cv2.imshow("Subtract", subtract)

cv2.waitKey(0)
cv2.destroyAllWindows()