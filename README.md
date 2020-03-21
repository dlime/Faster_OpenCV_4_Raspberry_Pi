# Faster OpenCV for Raspberry Pi
Leverage all your CPUs power in OpenCV by using **TBB**, **Neon** and **VFPV3** libraries.

Since I've already compiled this on my own Raspberry Pi I made it available on GitHub.

Save countless of compile time by just installing these debs. Enjoy!

## What is this?
* A pre-compiled **OpenCV 4.2.0** for **Raspberry Pi** optimized for deep learning / computer vision applications (**NEON**, **VFPV3**, **TBB** turned on).
* Bindings for **Python 2** and **Python 3** are also included.
* For detailed build informations click [here](build_information.txt).
* Created with OpenCV cpack targets.
* Tested on **Raspberry Pi 3** using **Raspbian Buster (Debian 10)** (for Raspbian Stretch click [here](https://github.com/dlime/Faster_OpenCV_4_Raspberry_Pi/releases/tag/stretch_410)).

## How much faster?
Performance tests have been made in this [great blog article](https://www.pyimagesearch.com/2017/10/09/optimizing-opencv-on-the-raspberry-pi/) which led to an approximate **30%** increase in speed and of over **48%** when applied strictly to DNN module.

Another performance test is available [here](https://www.theimpossiblecode.com/blog/faster-opencv-smiles-tbb/) which also led to about **30%** increase in speed.

## How to use it?
Install OpenCV library prerequisites on your Raspberry Pi.
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y \
	libjpeg-dev libpng-dev libtiff-dev libgtk-3-dev \
	libavcodec-extra libavformat-dev libswscale-dev libv4l-dev \
	libxvidcore-dev libx264-dev libjasper1 libjasper-dev \
	libatlas-base-dev gfortran libeigen3-dev libtbb-dev
```

Install **numpy** based on your target Python version:
```
sudo apt-get install -y python3-dev python3-numpy
```
or:
```
sudo apt-get install -y python-dev python-numpy
```

### How to install?
Clone the repo into your Raspberry Pi and install all debs:
```
git clone https://github.com/dlime/Faster_OpenCV_4_Raspberry_Pi.git
cd Faster_OpenCV_4_Raspberry_Pi/debs
sudo dpkg -i OpenCV*.deb
sudo ldconfig
```

### How to test?

#### C++
Test the installation by going to tests cpp test folder, build it and launch the executable:
```
cd Faster_OpenCV_4_Raspberry_Pi/tests/cpp_opencv_test
mkdir build && cd build
cmake ..
make -j`cat /proc/cpuinfo | grep -c 'processor'`
./cpp_opencv_test
```

#### Python
Test the installation by going to tests folder and launch the test.py file:
```
cd Faster_OpenCV_4_Raspberry_Pi/tests/python_opencv_test
python test.py
```

You shouldn't see any error messages in console and an image with tetris blocks with contours drawed should appear.

### How to uninstall?
Run the following command in your Raspberry Pi terminal:
```
sudo apt purge opencv-*
```
