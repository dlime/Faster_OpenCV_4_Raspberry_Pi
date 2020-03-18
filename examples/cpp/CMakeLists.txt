cmake_minimum_required(VERSION 3.1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

project(cpp_opencv_test)

find_package(OpenCV REQUIRED)

message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/tetris_blocks.png" DESTINATION "${CMAKE_BINARY_DIR}")
add_executable(cpp_opencv_test main.cpp)
target_link_libraries(cpp_opencv_test ${OpenCV_LIBS})
