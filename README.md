# OpenCV 4.1.0 for Raspberry Pi
* A pre-compiled **OpenCV 4.1.0** for **Raspberry Pi**, optimized for deep learning (**NEON**, **VFPV3**, **TBB** turned on).
* Bindings for **Python2** and **Python3** are also included.
* Created with OpenCV cpack targets
* Tested on **Raspberry Pi 3+** using **Raspbian Stretch (Debian 9)**

# Prerequisites
Before proceeding, install OpenCV library prerequisites.
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y
	libjpeg-dev libpng-dev libtiff-dev \
	libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
	libxvidcore-dev libx264-dev libjasper1 libjasper-dev \
	libgtk-3-dev \
	libatlas-base-dev gfortran \
	libeigen3-dev libtbb-dev
```

Install **numpy** based on your target Python version:
```
sudo apt-get install -y python3-dev python3-numpy
```
or:
```
sudo apt-get install -y python-dev python-numpy
```

# How to install OpenCV
Download and run dpkg on all the .deb in the repository:
```
git clone https://github.com/dlime/OpenCV_4_Raspberry_PI.git
cd OpenCV_4_Raspberry_PI
sudo dpkg -i OpenCV*
sudo ldconfig
```

# How to test
Go to test folder and launch the test.py file:
```
cd OpenCV_4_Raspberry_PI/test
sudo pip2 install imutils
python2 test.py
```

Or for Python 3:
```
cd OpenCV_4_Raspberry_PI/test
sudo pip3 install imutils
python3 test.py
```

# How to uninstall
```
sudo apt purge opencv-*
```
