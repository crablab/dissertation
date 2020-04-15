## Appendix 10: User Guide

This document provides a set of instructions for setting up, running and using the various software deliverables provided. 

Some hardware is required. It will be listed in the respective sections and provisions have been made with Dave Cohen (d.cohen@rhul.ac.uk) for it to be available over the summer. 

### Main software deliverable 

The main deliverable is a Python Flask application. This is provided with Dockerfiles to enable it to be run with ease on your machine. 

Requirements:

- Docker installation: https://docs.docker.com/get-docker/
- docker-compose: https://docs.docker.com/compose/install/

1) In the project directory, go to the `backend` directory. 
2) Execute `docker-compose up` and go and make a cup of tea!
3) Visit http://localhost:5000 to get the login page

To terminate `ctrl+c` and the containers will gracefully stop. The database is persisted. 

#### Using the website 

To create a new user you visit `/signup`. It is recommended to create a student and administrator account. 

You can then login as an administrator and create a new course with first lecture in the future. You can add further lectures if required. 

It is then possible on `/administrator` to assign students to a course. 

Logging in as a student, you see all upcoming lectures for all courses, and the next lecture. 

#### Running tests

As explained in the report, these are integration tests so in order to run them a local environment and database is required. 

One way to achieve this is to run just the MySQL container in Docker and then connect to that from your locally running tests. 

Requirements:

- Python3 
- Local installation of `requirements.txt` with Pip
- Installation of `pytest` using Pip 

1) Modify the connection string `backend/app/libraries/database.py` to refer to your instance of MySQL
2) Execute `pytest` in `backend/app/tests`

Alternatively, you can run both containers as described above and then enter the `web` container, kill the running Python process, install `pytest` and run the tests on that container. 

#### Common Issues

If you encounter any database connection issues then it's likely you just need to wait a little longer for the database to start. It is restarted several times when the container is being created and the website will be available long before it can connect to the database container. 

### `clicker_emulator` 

This software is made up of two parts:

- An Arduino sketch 
- A Python console to communicate with the Arduino

Requirements:

- Python3
- Arduino IDE 
- POSIX-compliant Operating System

#### Hardware 

Any Arduino should be sufficient to run this code. The project was carried out on a Nano328, however. A nRF24E1 is required and the pinout to connect it to the Arduino is in {@tbl1:table1}. 

#### Installation: Arduino 

The setup of the software environment on the computer is relatively simple and is based around the Arduino IDE which is available from: https://www.arduino.cc/en/main/software. It appears there is now an online version, but this has not been tested with this project. 

Once the Arduino IDE is installed you should try flashing the Arduino with the example "blink" code, available from File $\rightarrow$ Examples $\rightarrow$ Basic. 

Assuming you have installed the IDE correctly and have specified the serial port and Arduino type, a blinking status LED will be present.  

You can also compile and upload code from within other IDEs using plugins. VSCode has various plugins for this, setup of which is beyond the scope of this document. However, unintuitively, it is important that you set up a VSCode Workspace so the Arduino Sketch file (containing running preferences such as the serial port, baud rate etc.) can be created and saved. Otherwise, you cannot upload any code. 

To run the project code, two libraries are required:

- RF24 (a library to handle communication with the nRF24E1)
- FastCRC (to calculate the CRC checksums)

For the former, Sparkfun have published a guide on installation of the RF24 library into the correct folder in your filesystem: https://learn.sparkfun.com/tutorials/nrf24l01-transceiver-hookup-guide/arduino-code and you can download the RF24 library here: https://github.com/nRF24/RF24

The FastCRC library is installed in the same directory, and is downloadable here: https://github.com/FrankBoesing/FastCRC

You should then be able to verify and upload the project code! If you get library errors, ensure the libraries have been imported correctly and the IDE shows them in the GUI. 

The baud rate used in the project is 115200 - without that set correctly it will not be possible to communicate with the Arduino via the IDE's serial console. 

##### Frequent Issues

Two issues encountered and which took significant effort to identify the root cause of are included with some basic debugging. 

`fatal error: <library>: No such file or directory`

Check your libraries folder! The error will tell you which library is causing issues and it's important to note that each library should be in it's own folder, named identically to the `.h` file a directory down. Other subdirectories and files will be included. 

The expected structure is: 

```
- FastCRC
    - FastCRC.h
    - ...
- RF24
    - RF24.h
    - ... 
``` 

In the case that other libraries are missing, you should be able to install them in a similar fashion. 

`avrdude: stk500_getsync() attempt 1 of 10: not in sync: resp=0x00` 

This error occurs when either:

- The Arduino is disconnected or cannot be connected to: check the USB
- The wrong Arduino type is selected: check the board configuration and the type of CPU used 

`Cannot upload: device/resource busy`

This occurs when the serial connection to the serial port is already in use. Ensure you don't have any serial consoles open, or any of the Python scripts running. 
If that doesn't work, you may be specifying the wrong serial port. 

It is possible to identify a process using a serial port with `lsof` and then terminate this process using `pkill`. 

#### Installation: Python

The Python script is designed to work in Python 3, and not 2.7. 

The only library required and possibly not installed is PySerial, which is installed with `pip3 install pyserial`. 

When running the script, if any issues are encountered with packages then installing these with Pip should resolve them. 

#### Running 

The Arduino requires nothing except the presence of a power source to run. The code is in a constant loop and to reset the device (on the Nano) there is a button on the top. When the serial bus is active a red LED will flash. 

Execute the Python script in your terminal:

`python3 cli.py`

And when prompted, enter the numeral of the Arduino:

```
[0] /dev/ttyUSB0 - USB2.0-Serial
[1] /dev/ttyACM0 - Sierra Wireless EM7345 4G LTE - Sierra Wireless EM7345 4G LTE
Enter number of chosen serial device: 0
``` 

(It can be helpful to run the script without the Arduino connected, terminate with `ctrl + c` and then try again with the device connected, to deduce which device the Arduino is)

When using a Turning Point Clicker in the vicinity on the default channel (41), you will then see log lines appear. 

More options are described by running `python3 cli.py --help` 

### `device_fingerprinting` 

This is a basic demonstration page to show two different libraries used for browser fingerprinting. 

Requirements:

- Modern (eg. latest stable version) browser 

#### Running

Simply open the `index.html` file in your web browser. Two hashes which serve as the fingerprint will be displayed. 

You can see how well the libraries work by opening the page across different tabs, in "incognito" modes and in other browsers. 

### `crytographic_signing` 

This is a simple wrapper (an adaptor pattern) of a Ecliptic Curve signature algorithm. 

Requirements:
- Python 3

#### Installation 

The only dependency is on the ECDSA library, which can be installed with Pip `pip3 install ecdsa`. 

If you wish to run the tests you will need Pytest: `pip3 install pytest`. 

#### Running

As this is intended as an adaptor, it is structured as a library. You can execute the tests by running `pytest` in the directory. 

### `hm10-investigations` 

Originally, the HM-10 was intended to be connected to a Raspberry Pi but using a serial (RS232 TTL) to USB converter, you can connect it to a computer. 

1) Install Python3 and pip (the package manager) for your operating system: `sudo apt install python3 python3-pip`
2) Use pip to install the `pyserial` library: `pip3 install pyserial` 
3) Modify the `initial_test.py` script to use whichever port you have the HM-10 connected to (identified with `lsusb`)
4) Execute the script with `python3 initial_test.py`

You can also connect directly to the HM-10's port with `screen`, `minicom` or any other similar utility. 

Using one of the BLE apps described in the report, you can then connect to the BLE device and observe sending data to the BLE device and receiving it on the serial port. 