'''
A series of basic filters. Will be printed out in the same window. To save one,
Choose the number associated with it. Otherwise press RETURN to exit.

By Ben Hardy
'''

import cv2
import numpy
import sys
from matplotlib import pyplot

# load in the image
if len(sys.argv) == 1: # If there are no arguments, just load the default image
    img = cv2.imread('what.png', -1)
elif len(sys.argv) == 2: # load image at path with default imread val
    img = cv2.imread(sys.argv[1])
elif len(sys.argv) == 3: # load image using flag. Useful for opening grayscale
    img = cv2.imread(sys.argv[1], int(sys.argv[2]))

# simple 3x3 averaging filter
h = numpy.ones((3,3), numpy.float32)/9

# run the filter using filter2D. Image depth will be the same so use -1
avg = cv2.filter2D(img, -1, h)

# use the built in Gaussian filter to get a 3x3 gaussian filter and filter the
# image
gauss = cv2.GaussianBlur(img, (3,3), -1)

# Use the built in median filtering function to get do a median filter with a
# 3x3 filter
med = cv2.medianBlur(img, 3)

print ("To save an image with a filter, input the number from beside the\n" 
       "title after into the terminal after exiting the plot window.\n"
       "Otherwise just hit RETURN.")
# Plot the 4 images.
pyplot.subplot(221)
pyplot.imshow(img)
pyplot.title('0:Original Image')

pyplot.subplot(222)
pyplot.imshow(avg)
pyplot.title('1:Averaging Filter')

pyplot.subplot(223)
pyplot.imshow(gauss)
pyplot.title('2:Gaussian Blur')


pyplot.subplot(224)
pyplot.imshow(med)
pyplot.title('3:Median Filter')

pyplot.show()

# read in input. If it is anything other than 1,2 or 3, then simply exit.
# otherwise save the image associated with that number.
res = raw_input();
if res == "":
    print('Not saving anything')
elif int(res) == 1:
    cv2.imwrite('avgfiltimg.png', avg)
    print('Saved image as avgfiltimg.png')
elif int(res) == 2:
    cv2.imwrite('gaussimg.png', gauss)
    print('Saved image as gaussimg.png')
elif int(res) == 3:
    cv2.imwrite('medfiltimg.png', avg)
    print('Saved image as medfiltimg.png')
else:
    print('Not saving anything')


