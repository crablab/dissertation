// Example from the documentation: https://developers.google.com/web/updates/2016/03/access-usb-devices-on-the-web

// Third-party WebUSB Arduino library
#include <WebUSB.h>

WebUSB WebUSBSerial(1 /* https:// */, "webusb.github.io/arduino/demos");

#define Serial WebUSBSerial

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // Wait for serial port to connect.
  }
  Serial.write("WebUSB FTW!");
  Serial.flush();
}

void loop() {
  // Nothing here for now.
}
