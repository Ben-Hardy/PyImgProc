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
if len(sys.argv) == 1: # If there are no arguments, just load the default image
    img = cv2.imread('what.png')
elif len(sys.argv) == 2: # load image at path with default imread val
    img = cv2.imread(sys.argv[1])
elif len(sys.argv) == 3: # load image using flag. Useful for opening grayscale
    img = cv2.imread(sys.argv[1], int(sys.argv[2]))
cv2.imshow('result', img) # show the result

cv2.waitKey(0) # listen for a key press

cv2.destroyAllWindows() # upon hearing key press, close the image window
