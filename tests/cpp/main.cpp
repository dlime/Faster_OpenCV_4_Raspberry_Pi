/**
 * Author: Dario Limongi
 * License: BSD-2 (please check LICENSE file in repo root.)
 */

#include <iostream>
#include <opencv2/opencv.hpp>

namespace
{
const int CURRENT_OPENCV_BUILD_MAJOR{ 4 };
const int CURRENT_OPENCV_BUILD_MINOR{ 2 };
const int CURRENT_OPENCV_BUILD_REVISION{ 0 };
} // namespace

bool
test_build_version( )
{
    if ( cv::getVersionMajor( ) != CURRENT_OPENCV_BUILD_MAJOR ) {
        std::cout << "ERROR: OpenCV version is different than the expected." << std::endl;
        return false;
    }

    if ( cv::getVersionMinor( ) != CURRENT_OPENCV_BUILD_MINOR ) {
        std::cout << "ERROR: OpenCV version is different than the expected." << std::endl;
        return false;
    }


    if ( cv::getVersionRevision( ) != CURRENT_OPENCV_BUILD_REVISION ) {
        std::cout << "ERROR: OpenCV version is different than the expected." << std::endl;
        return false;
    }

    return true;
}

bool
test_multithreading_enabled( )
{
    if ( cv::getNumThreads( ) < 1 ) {
        std::cout << "ERROR: Available threads should be more than 1" << std::endl;
        return false;
    }

    if ( cv::getNumThreads( ) < cv::getNumberOfCPUs( ) ) {
        std::cout << "ERROR: TBB is not enabled." << std::endl;
        return false;
    }

    return true;
}

bool
test_neon_enabled( )
{
    if ( cv::checkHardwareSupport( CV_CPU_NEON ) == 0 ) {
        std::cout << "ERROR: NEON is not enabled." << std::endl;
        return false;
    }

    return true;
}

int
run_tests( )
{
    if ( !test_build_version( ) ) {
        return -1;
    }

    if ( !test_multithreading_enabled( ) ) {
        return -1;
    }

    if ( !test_neon_enabled( ) ) {
        return -1;
    }

    return 0;
}

// Simple "test framework" to avoid setting up GoogleTest on CI
int
main( )
{
    return run_tests( );
}
