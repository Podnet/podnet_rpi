<p align="center">

<img src="https://thepodnet.com/images/press-images/facebook-banner-podnet.png" />

# Podnet RPi

[![PyPI](https://img.shields.io/pypi/pyversions/podnet_rpi?logo=orange&style=for-the-badge)](https://pypi.org/project/podnet-rpi/)
![License](https://img.shields.io/github/license/podnet/podnet_rpi?style=for-the-badge)
![PyPI Version](https://img.shields.io/pypi/v/podnet_rpi?color=yellow&style=for-the-badge)
![Wheel](https://img.shields.io/pypi/wheel/podnet_rpi?color=red&style=for-the-badge)
![Status](https://img.shields.io/pypi/status/podnet_rpi?style=for-the-badge)


Client library for Raspberry Pi devices for communicating with the Pod Network.

## Installation
Right now the installation process is very long. We are working on building a setup script that makes it easy for everyone to install Podnet Library on their Raspberry Pi devices.
This guide assumes that you have **already logged into your Raspberry Pi via SSH**.

1. Update your RPi
```console
pi@raspberrypi:~$ sudo apt-get update && sudo apt-get upgrade -y
```

2. Clone the repository to your RPi device
```console
pi@raspberrypi:~$ git clone https://github.com/Podnet/podnet_rpi.git
```

3. Fetch all submodules 
```console
$ cd podnet_rpi/

$ git submodule update --init
```

4. Install dependencies
```console
$ cd podnet_rpi/libraries/RF24/

$ sudo make install

$ sudo apt-get install python-dev libboost-python-dev
```

5. Manually link Boost library for Python 3
```console
$ sudo ln -s /usr/lib/arm-linux-gnueabihf/libboost_python-py<version>.so /usr/lib/arm-linux-gnueabihf/libboost_python3.so
```
Possible values of **<version>** can be 34, 35, 36 depending upon the python installation.

6. Install **setuptools**
```console
$ sudo apt-get install python3-setuptools
```

7. Install **RF24** library for Python
```console
$ cd pyRF24/

$ python3 setup.py build

$ sudo python3 setup.py install
```

8. Install RF24Network Library
```console
$ cd ~/podnet_rpi/libraries/RF24Network/

$ sudo make install
```

9. Install RF24Network Library for Python
```console
$ cd ~/podnet_rpi/libraries/RF24/pyRF24/pyRF24Network/

$ python3 setup.py build

$ sudo python3 setup.py install
```

10. All dependencies are finally installed, we can proceed to install **podnet_rpi** package
```console
$ pip install podnet_rpi
```


## Examples
Execute examples from **examples/** directory.


## How to Contribute

1. Clone repo and create a new branch: `$ git checkout https://github.com/alichtman/stronghold -b name_for_new_branch`.
2. Make changes and test
3. Submit Pull Request with comprehensive description of changes
