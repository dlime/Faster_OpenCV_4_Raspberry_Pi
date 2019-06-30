# OpenCV 4.1.0 for Raspberry Pi
* A pre-compiled **OpenCV 4.1.0** for **Raspberry PI**, optimized for deep learning (**NEON** and **VFPV3** turned on). 
* Bindings for **Python2** and **Python3** are also included.
* Created with OpenCV cpack targets
* Tested on **Raspberry Pi 3+** on **Raspbian Stretch**

# Prerequisites
Before proceeding, install the OpenCV library prerequisites.
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y libtiff5-dev libjasper-dev libpng12-dev libjpeg-dev \
libavcodec-dev libavformat-dev libswscale-dev \
libv4l-dev libgtk2.0-dev libatlas-base-dev gfortran
```

Install numpy based on your Python version:
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
python2 test.py
```

Or for Python 3:
```
python3 test.py
```

# Future development
* Include TBB
