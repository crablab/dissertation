1) Configure VS code with Arduino plugin 
2) Ensure workspace is loaded/created otherwise the sketch file won't be created with settings
3) Specify board and serial port
4) Grab the required libraries
    - RF24: https://github.com/nRF24/RF24
        - It seems the accepted way to do this is loading it directly into the Arduino library folders. 
        - https://learn.sparkfun.com/tutorials/nrf24l01-transceiver-hookup-guide/arduino-code
        - Ensure that code is not within another folder!
    - FastCRC
        - https://github.com/FrankBoesing/FastCRC
        - Do the same as the above and install to the Arduino libraries folder 
5) Try to verify & upload 
6) Wire up the NRF to the Arduino 
    - Diagram... 
    - IRQ goes nowhere 

Troubleshooting:

### avrdude: stk500_getsync() attempt 1 of 10: not in sync: resp=0x00

- Reset Arduino/check USB
- Check board config and processor version