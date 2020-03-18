/**
 * Author: Dario Limongi
 * License: BSD-2 (please check LICENSE file in repo root.)
 * Adapted from:
 * https://www.pyimagesearch.com/2015/08/10/checking-your-opencv-version-using-python/
 */

#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>

namespace
{
const std::string IMAGE{ "tetris_blocks.png" };
}

void
show_build_info( )
{
    std::cout << "OpenCV version: " << cv::getVersionMajor( ) << "." << cv::getVersionMinor( ) << "."
              << cv::getVersionRevision( ) << std::endl;

    std::cout << "Available CPUs: " << cv::getNumberOfCPUs( ) << std::endl;
    std::cout << "Available threads: " << cv::getNumThreads( ) << std::endl;
    std::cout << "Cpu NEON support: " << cv::checkHardwareSupport( CV_CPU_NEON ) << std::endl;
}

int
main( )
{
    show_build_info( );

    auto image = cv::imread( IMAGE );
    if ( !image.data ) {
        std::cout << "ERROR: Could not open or find the image" << std::endl;
        return 1;
    }

    cv::Mat gray_image, thresholded_image;
    cv::cvtColor( image, gray_image, cv::COLOR_BGR2GRAY );
    cv::threshold( gray_image, thresholded_image, 225, 255, cv::THRESH_BINARY_INV );

    std::vector< std::vector< cv::Point > > contours;
    cv::findContours( thresholded_image, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE );
    cv::drawContours( image, contours, -1, cv::Scalar( 240, 0, 159 ), 3 );

    cv::imshow( "Image", image );
    cv::waitKey( 0 );

    return 0;
}
