'''
Test program to make sure cv2 and numpy are working. 
Based on a simple tutorial. Run this before trying anything else
to make sure your setup is function. This is all Python 2.7.

By Ben Hardy
'''

import cv2
import numpy
import sys

print("Click the image and press a key to exit.\n")
if len(sys.argv) == 1:
    img = cv2.imread('what.png')
elif len(sys.argv) > 1:
    img = cv2.imread(sys.argv[1])
cv2.imshow('result', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
