# Raspberry Pi Home Security Control System with User Recognition
# by: Aosen Ba, Runfeng Chen, Chang Qin, Zhixiang Ren

The project is a Raspberry Pi Web controlled home security system. It has three parts which are gateway control, user recognition, and Web GUI control. The first part allows user to unlock the door (represented by solenoid) by verifying his fingerprint. User recognition part will send the user a email with snapshot for warning if it detects motion. Web GUI is designed to make user able to get live stream video from multiple Raspberry Pi Cameras, change shooting angles, and even take a picture by clicking a button. If the user finds a invader, he can send different sound alerts to home from the Web GUI.

## Flow Diagram
![flow diagram](https://user-images.githubusercontent.com/25835420/39506651-064482c6-4da8-11e8-8052-99cbfb08e145.jpg)

## Components
- [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [Raspberry Pi Camera Module V2](https://www.raspberrypi.org/products/camera-module-v2/)
- [mbed](https://os.mbed.com/platforms/mbed-LPC1768/)
- [Fingerprint Scanner](https://os.mbed.com/users/beanmachine44/notebook/fingerprint-scanner1/)
- [SD Card Reader](https://os.mbed.com/cookbook/SD-Card-File-System)
- [Speaker](https://os.mbed.com/users/4180_1/notebook/using-a-speaker-for-audio-output/)
- [Class D Audio Amp](https://os.mbed.com/users/4180_1/notebook/tpa2005d1-class-d-audio-amp/)

## Demo Video
