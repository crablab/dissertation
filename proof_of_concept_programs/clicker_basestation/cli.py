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
import argparse
import re
import signal
import csv

parser = argparse.ArgumentParser(description='Base station emulation for Response Card')
parser.add_argument('--verbose', action='store_true',
                    help='Set logging verbosity')
parser.add_argument('--output', action='store',
                    help='Provide output file to be written to (CSV)')
# Constants
INPUT_LENGTH = 60
INCOMING_RE = r"^incoming: (.{12}) --> (.)"
# Global variables
file = None
decoded = []

def decode(line):
    """
    Decodes lines from the clicker base station Arduino to parse addresses and button inputs.
    This function is essentially a direct adaption of line 50 from Nick Mooney's original work
    The regular expression used was written by him 
    :param line: The line from the Arduino serial port to decode
    """

    # Handle as UTF-8 and do the Regex match
    line = line.decode("utf-8")
    result = re.match(INCOMING_RE, line)
    
    if result:
        groups = result.groups()
        data, button = groups
        data_dict = {"address_from": data[:6], "address_to": data[6:12], "button": button}
        return(data_dict)
    else:
        return None

def signal_handler(signal, frame):
    """
    Catches `ctrl + c` and handles gracefully to write CSV to disc 
    Based on StackOverflow answer: https://stackoverflow.com/a/57787316
    """
    print("Exiting...")

    if(file):
        writer = csv.DictWriter(file, decoded[0].keys())
        writer.writeheader()
        writer.writerows(decoded)
        file.close()
        print("Written to file successfully")

    sys.exit(0)

def open_file(path):
    return open(path,"w+")

if __name__ == "__main__":
    # SIGINT handler to allow graceful shutdown 
    signal.signal(signal.SIGINT, signal_handler)
    
    args = parser.parse_args()
    ports = serial.tools.list_ports.comports()
    
    if len(ports) == 0:
        sys.exit("No serial bus devices")

    for n, port in enumerate(ports):
        print("[" + str(n) + "] " + str(port))

    chosen_value = int(input("Enter number of chosen serial device: "))
    
    port = serial.Serial(ports[chosen_value][0], baudrate = 115200, timeout = .25)

    # If we need to, open a file
    if(args.output):
        try:
            file = open_file(args.output)
        except:
            exit("Path " + str(args.output) + " could not be written to")

    while True:
        if port.inWaiting():
            from_board = port.read(INPUT_LENGTH)
            lines = from_board.split(b"\n")
            
            for line in lines:
                # Get data with correct charset and then decode lines
                # of useful clicker input
                line_decoded = decode(line)
                if(args.verbose):
                    print(line_decoded)
                if(line_decoded != None):
                    print("Data received")
                    decoded.append(line_decoded)

