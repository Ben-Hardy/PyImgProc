import cv2
import numpy

print("Press ESC to exit.\n")

img = cv2.imread('aurora.png')

cv2.imshow('result', img)
r = cv2.waitKey(0) & 0xFF

if r == 27:
	cv2.destroyAllWindows()
