cmake_minimum_required(VERSION 3.1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

project(cpp_opencv_test)

enable_testing()

find_package(OpenCV REQUIRED)

add_executable(cpp_opencv_test main.cpp)

target_link_libraries(cpp_opencv_test ${OpenCV_LIBS})

add_test(NAME CppOpenCVTest COMMAND cpp_opencv_test)
