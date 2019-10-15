#!/usr/bin/env python3

"""
Based on MIDI version by:
    Nick Mooney
    nmooney@cs.washington.edu
    https://github.com/nickmooney/turning-clicker/blob/master/simple_clicker_midi.py
Adapted to remove MIDI logic
"""

import serial
import serial.tools.list_ports
import sys
import re
import subprocess
import time

INPUT_LENGTH = 60
INCOMING_RE = r"^incoming: (.{12}) --> (.)"

if __name__ == "__main__":
    ports = serial.tools.list_ports.comports()
    
    if len(ports) == 0:
        sys.exit("No serial bus devices")

    for n, port in enumerate(ports):
        print("[" + str(n) + "] " + str(port))

    chosen_value = int(input("Enter number of chosen serial device: "))
    
    port = serial.Serial(ports[chosen_value][0], baudrate = 115200, timeout = .25)

    while True:
        if port.inWaiting():
            from_board = port.read(INPUT_LENGTH)
            lines = from_board.split(b"\n")
            for line in lines:
                print(line.decode("utf-8"))
