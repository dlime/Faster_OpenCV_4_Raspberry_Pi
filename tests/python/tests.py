# Author: Dario Limongi
# License: BSD-2 (please check LICENSE file in repo root.)

import cv2

CURRENT_OPENCV_BUILD_VERSION = [4, 2, 0]


def test_build_version():
    assert cv2.getVersionMajor() == CURRENT_OPENCV_BUILD_VERSION[0]
    assert cv2.getVersionMinor() == CURRENT_OPENCV_BUILD_VERSION[1]
    assert cv2.getVersionRevision() == CURRENT_OPENCV_BUILD_VERSION[2]


def test_multithreading_enabled():
    assert cv2.getNumThreads() > 1
    assert cv2.getNumThreads() == cv2.getNumberOfCPUs()


def test_neon_enabled():
    # Value taken from doc. OpenCV CPU labels don't work correctly in Python
    cv2.CPU_NEON = 100
    assert not cv2.checkHardwareSupport(cv2.CPU_NEON)
