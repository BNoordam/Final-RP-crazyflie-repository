# Final-RP-crazyflie-repository
Ubuntu version=23.10

python3 version=3.11.6

USER must have sudo rights.

## Installing the Linux driver for the WiFi dongle

Commands for installing the Edimax AC600 Wi-Fi USB adapter
```
Sudo apt-get update
Sudo apt-get install DKMS
sudo apt install git build-essential bc libelf-dev 
git clone  https://github.com/aircrack-ng/rtl8812au.git
cd rtl8812au
sudo make dkms_install
sudo modprobe 8812au
Sudo reboot
```

## Other package dependencies

```
Sudo apt-get update
Sudo apt-get install cmake
sudo apt install git python3-pip libxcb-xinerama0 libxcb-cursor0
pip3 install --upgrade pip
pip3 install cfclient
pip3 install pandas
pip3 install matplotlib
pip3 install numpy
git clone https://github.com/bitcraze/crazyflie-lib-python.git
cd crazyflie-lib-python
pip3 install -e .
```

## Hierarchy
First, install the package dependencies in this README. Then flash the crazyflie-firmware  

Before running the trajectory following scripts:
- Install the Linux driver for the WiFi dongle
- Setup the loco positioning system following https://www.bitcraze.io/documentation/tutorials/getting-started-with-loco-positioning-system/
- Setup the AI deck following the instructions in the aideck-gap8-examples repository.
- Install uav_trajectories
- Generate trajectories for the Crazyflie to follow in uav_trajectories.

The logged position data can be used in the data processing scripts (also located in trajectory scripts). And the saved images in the NN from the deep-multirobot repository.





