import serial 
import threading

conn = serial.Serial('/dev/ttyUSB1', 115200)

# Some example code: https://stackoverflow.com/a/56632812
class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)
    
def serial_read(sread):
    while True:
        print(sread.readline())

def serial_send():
    if(input()):
        # conn.write(str.encode("160"))
        # conn.write(str.encode("160"))
        # conn.write(str.encode("160"))
        conn.write(str.encode("\r"))
        print("sent data")

if __name__ == "__main__":
    sread = ReadLine(conn)

    read = threading.Thread(target=serial_read, args=[sread])
    send = threading.Thread(target=serial_send)

    read.start()
    send.start()
