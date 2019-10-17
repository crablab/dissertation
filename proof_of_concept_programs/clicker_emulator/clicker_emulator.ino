/*
 * Clicker Emulator for Turning Technologies Response Card
 * 
 * Based on the basestation written by:
 * Nick Mooney
 * nmooney@cs.washington.edu
 *
 * Depends on both the excellent TMRh20 RF24 library[0]
 * and the FastCRC library[1].
 *
 * [0]: https://github.com/TMRh20/RF24
 * [1]: https://github.com/FrankBoesing/FastCRC
 */

#include <SPI.h>
#include <RF24.h>
#include <printf.h>
#include <FastCRC.h>
#include <FastCRC_cpu.h>
#include <FastCRC_tables.h>

#define ADDR_WIDTH 3
// An address, a byte, and a 2-byte CRC
// go into a buffer, hence address width + 3
#define BUFSIZE (ADDR_WIDTH + 3)
#define CHANNEL 41
#define OUTGOING_COPIES 5

uint8_t baseAddress[] = {0x56, 0x34, 0x12};
RF24 radio(7, 8);
FastCRC16 CRC16;

byte incomingData[BUFSIZE];
byte outgoingData[BUFSIZE];
byte crcBuffer[BUFSIZE + 3];
String readString;

void setup() {
  Serial.begin(115200);
  Serial.println(F("*** booting ***"));
  printf_begin();

  radio.begin();

  // All the Turning-specific configuration
  radio.setPALevel(RF24_PA_HIGH);
  radio.setAutoAck(false);
  radio.disableCRC();
  radio.setPayloadSize(BUFSIZE);
  radio.setDataRate(RF24_1MBPS);
  radio.setChannel(CHANNEL);
  radio.setAddressWidth(3);
  radio.openReadingPipe(1, baseAddress);

  // Set up data structures
  memset(incomingData, 0, BUFSIZE);
  memset(outgoingData, 0, BUFSIZE);
  crcBuffer[0] = baseAddress[2];
  crcBuffer[1] = baseAddress[1];
  crcBuffer[2] = baseAddress[0];

  // Ready set go
  radio.startListening();
  radio.printDetails();
  Serial.println();
  Serial.println();
}

void loop() {
  // While the Serial connection is open
  while (Serial.available()) {
    // Get data from Serial until newline
    readString = Serial.readStringUntil('\r');
    
    // Check does not exceed null-terminated buffer
    if(readString.length() > BUFSIZE){
      Serial.println("overflow");
      break;
    } else if (radio.available()) {
      // Do something with that address
      readString.getBytes(incomingData, BUFSIZE);
      quickWrite(0x06, incomingData);
      // Reset buffers
      readString = "";
      memset(incomingData, 0, BUFSIZE);
      Serial.println(F("sent"));
    }
  }
}

// Given a pointer to a data array (which should contain a source
// clicker MAC, a data byte, and two CRC bytes), check that the CRC
// is correct. Note that the CRC (for packets received from the clicker, NOT
// packets sent to the clicker) is actually calculated from 
// an array of base station MAC, clicker MAC, and the data byte.
bool verifyCRC(byte *data) {
  // Bytes below ADDR_WIDTH should never change
  // in the CRC buffer. Copy over an address + a single byte.
  memcpy(&crcBuffer[ADDR_WIDTH], data, ADDR_WIDTH + 1);
  uint16_t checksum = CRC16.ccitt(crcBuffer, 7);
  uint16_t received_checksum = (data[ADDR_WIDTH + 1] << 8) + data[ADDR_WIDTH + 2];
  return (received_checksum == checksum);
}

// Writes out the byte b with the given clicker address
// as its destination -- handles checksumming, manages the
// radio, and automatically sends several copies. Good for
// acknowledging clicker packets so the clicker doesn't keep
// re-sending the same thing.
void quickWrite(byte b, uint8_t *address) {
  outgoingData[0] = address[0];
  outgoingData[1] = address[1];
  outgoingData[2] = address[2];
  outgoingData[3] = b;
  uint16_t checksum = CRC16.ccitt(outgoingData, 4);
  outgoingData[4] = (checksum >> 8) & 0xFF;
  outgoingData[5] = checksum & 0xFF;

  Serial.print(F("outgoing: "));
  for (int i = 0; i < BUFSIZE; i++) {
    printf("%02x", outgoingData[i]);
  }
  Serial.println();

  // Stop listening long enough to write our response
  radio.stopListening();
  radio.openWritingPipe(address);
  for (int i = 0; i < OUTGOING_COPIES; i++) {
    radio.write(outgoingData, BUFSIZE);
  }
  radio.startListening();
}
