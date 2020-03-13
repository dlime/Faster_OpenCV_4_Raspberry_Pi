# Author: Dario Limongi
# License: BSD-2 (please check LICENSE file in repo root.)
# Adapted from: https://www.pyimagesearch.com/2015/08/10/checking-your-opencv-version-using-python/

from __future__ import print_function
import cv2
import sys

CURRENT_OPENCV_BUILD_VERSION = [4, 2, 0]


def check_build_info():
    success = True

    print("OpenCV Version: {}".format(cv2.__version__))
    if (cv2.getVersionMajor() != CURRENT_OPENCV_BUILD_VERSION[0]) and (
            cv2.getVersionMinor() != CURRENT_OPENCV_BUILD_VERSION[1]) and (
            cv2.getVersionRevision() != CURRENT_OPENCV_BUILD_VERSION[2]):
        print("ERROR: OpenCV version is different than the expected.")
        success = False

    print("Available CPUs: ", cv2.getNumberOfCPUs())
    print("Available threads: ", cv2.getNumThreads())
    if cv2.getNumThreads() < cv2.getNumberOfCPUs():
        print("ERROR: TBB is not enabled.")
        success = False

    cv2.CPU_NEON = 100  # Value taken from OpenCV doc. CPU labels don't work correctly in Python
    print("Cpu NEON support: ", cv2.checkHardwareSupport(cv2.CPU_NEON))
    if not cv2.checkHardwareSupport(cv2.CPU_NEON):
        print("ERROR: NEON is not enabled.")
        success = False

    return success


def main():
    if not check_build_info():
        print("FAIL: You are using OpenCV without NEON/TBB support enabled.")
        sys.exit(1)
    print("SUCCESS: You are using latest OpenCV version, with NEON/TBB support enabled.")

    image = cv2.imread("tetris_blocks.png")
    if not image.data:
        print("ERROR: Could not open or find the image")
        sys.exit(1)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(gray_image, 225, 255, cv2.THRESH_BINARY_INV)[1]
    (contours, _) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw the contours on the image
    cv2.drawContours(image, contours, -1, (240, 0, 159), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
