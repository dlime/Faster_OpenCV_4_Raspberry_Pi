# Author: Dario Limongi
# License: BSD-2 (please check LICENSE file in repo root.)
# Adapted from: https://www.pyimagesearch.com/2015/08/10/checking-your-opencv-version-using-python/

from __future__ import print_function
import cv2

print("OpenCV Version: {}".format(cv2.__version__))
image = cv2.imread("tetris_blocks.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# draw the contours on the image
cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)
