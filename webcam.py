# -*- coding: utf-8 -*-
import numpy as np
import cv2

def precesamiento(image):
	# Convertir a escala de grises
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	image_gray_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)

	canny_edges = cv2.Canny(image_gray_blur, 10, 40)

	ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
	return mask

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read()
	cv2.imshow('Procesamiento', precesamiento(frame))
	if cv2.waitKey(1) == 13:
		# 13 es Enter
		break

capture.release()
cv2.destroyAllWindows()
