import serial 
import threading

conn = serial.Serial('/dev/ttyUSB1', 115200)

def serial_read():
    while True:
        bytesToRead = conn.inWaiting()
        conn.read(bytesToRead)

def serial_send():
    if(input()):
        # conn.write(str.encode("160"))
        # conn.write(str.encode("160"))
        # conn.write(str.encode("160"))
        conn.write(str.encode("\r"))
        print("sent data")

if __name__ == "__main__":
    serial_read.start()
    serial_send.start()
