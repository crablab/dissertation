## Appendix 0: Python script for base station emulation

```python
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
```

## Appendix 1: HTML for Browser Fingerprinting test

```html
<html>

<head>
    <title>Device Fingerprinting</title>
    <!-- Source: https://github.com/Valve/fingerprintjs2-->
    <script type="text/javascript" src="fingerprint2.js"></script>
    <!-- Source: https://github.com/jackspirou/clientjs-->
    <script src="client.min.js"></script>
</head>

<body>
    <h1>Your Fingerprint2 is: <code id="fp1"></code></h1>
    <h1>Your ClientJS fingerprint is: <code id="fp2"></code></h1>
</body>

</html>
```

## Appendix 2: JavaScript for Browser Fingerprinting test

```javascript
setTimeout(function() {
    // Fingerprint 2
    var options = {
        excludes: {
            userAgent: true,
            language: true
        }
    }
    // Based off https://github.com/Valve/fingerprintjs2#usage
    Fingerprint2.get(options, function(components) {
        var values = components.map(function(component) {
            return component.value
        })
        var murmur = Fingerprint2.x64hash128(values.join(''), 31)

        document.getElementById("fp1").innerHTML = murmur;
    })

    // ClientJS
    var client = new ClientJS();

    var fingerprint = client.getFingerprint();

    document.getElementById("fp2").innerHTML = fingerprint;

}, 500)
```

## Appendix 3: student ID full tag output 

```
** TagInfo scan (version 4.24.5) 2019-11-27 17:44:39 **
Report Type: External

-- IC INFO ------------------------------

# IC manufacturer:
NXP Semiconductors

# IC type:
MIFARE Classic EV1 (MF1S50)

-- NDEF ------------------------------

# No NDEF data storage present:
Maximum NDEF storage size after format: 716 bytes

-- EXTRA ------------------------------

# Memory size:
1 kB
* 16 sectors, with 4 blocks per sector
* 64 blocks, with 16 bytes per block

# IC detailed information:
Full product name: MF1S507xX/V1

# Originality check:
Signature verified with NXP public key

-- FULL SCAN ------------------------------

# Technologies supported:
MIFARE Classic compatible
ISO/IEC 14443-3 (Type A) compatible
ISO/IEC 14443-2 (Type A) compatible

# Android technology information:
Tag description:
* TAG: Tech [android.nfc.tech.NfcA, android.nfc.tech.MifareClassic, android.nfc.tech.NdefFormatable]
* Maximum transceive length: 253 bytes
* Default maximum transceive time-out: 618 ms

# Detailed protocol information:
ID: E2:F8:0C:77
ATQA: 0x0400
SAK: 0x08

# Memory content:
Sector 0 (0x00)
[00] r--  E2 F8 0C 77 61 88 04 00 C8 23 00 20 00 00 00 18 |...wa....#. ....|
[01] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[02] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[03] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 1 (0x01)
[04] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[05] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[06] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[07] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 2 (0x02)
[08] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[09] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[0A] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[0B] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 3 (0x03)
[0C] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[0D] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[0E] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[0F] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 4 (0x04)
[10] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[11] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[12] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[13] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 5 (0x05)
[14] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[15] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[16] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[17] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 6 (0x06)
[18] ???  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
[19] ???  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
[1A] ???  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
[1B] ???  XX:XX:XX:XX:XX:XX --:--:-- -- XX:XX:XX:XX:XX:XX
          (unknown key)                 (unknown key)

Sector 7 (0x07)
[1C] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[1D] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[1E] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[1F] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 8 (0x08)
[20] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[21] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[22] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[23] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 9 (0x09)
[24] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[25] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[26] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[27] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 10 (0x0A)
[28] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[29] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[2A] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[2B] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 11 (0x0B)
[2C] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[2D] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[2E] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[2F] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 12 (0x0C)
[30] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[31] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[32] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[33] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 13 (0x0D)
[34] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[35] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[36] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[37] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 14 (0x0E)
[38] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[39] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[3A] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[3B] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

Sector 15 (0x0F)
[3C] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[3D] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[3E] rwi  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
[3F] wxx  FF:FF:FF:FF:FF:FF FF:07:80 69 FF:FF:FF:FF:FF:FF
          Factory default key           Factory default key (readable)

r/R=read, w/W=write, i/I=increment,
d=decr/transfer/restore, x=r+w, X=R+W
data block: r/w/i/d:key A|B, R/W/I:key B only,
  I/i implies d, *=value block
trailer (order: key A, AC, key B): r/w:key A,
  W:key B, R:key A|B, (r)=readable key
AC: W implies R+r, R implies r

--------------------------------------
```

## Appendix 4: Minicom output

```
--- Miniterm on /dev/ttyAMA0  9600,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---

--- pySerial (3.4) - miniterm - help
---
--- Ctrl+]   Exit program
--- Ctrl+T   Menu escape key, followed by:
--- Menu keys:
---    Ctrl+T  Send the menu character itself to remote
---    Ctrl+]  Send the exit character itself to remote
---    Ctrl+I  Show info
---    Ctrl+U  Upload file (prompt will be shown)
---    Ctrl+A  encoding
---    Ctrl+F  edit filters
--- Toggles:
---    Ctrl+R  RTS   Ctrl+D  DTR   Ctrl+B  BREAK
---    Ctrl+E  echo  Ctrl+L  EOL
---
--- Port settings (Ctrl+T followed by the following):
---    p          change port
---    7 8        set data bits
---    N E O S M  change parity (None, Even, Odd, Space, Mark)
---    1 2 3      set stop bits (1, 2, 1.5)
---    b          change baud rate
---    x X        disable/enable software flow control
---    r R        disable/enable hardware flow control

--- Settings: /dev/ttyAMA0  9600,8,N,1
--- RTS: active    DTR: active    BREAK: inactive
--- CTS: active    DSR: inactive  RI: inactive  CD: inactive
--- software flow control: inactive
--- hardware flow control: inactive
--- serial input encoding: UTF-8
--- serial output encoding: UTF-8
--- EOL: CRLF
--- filters: default
--- local echo active ---
AT
ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC

--- Settings: /dev/ttyAMA0  9600,8,N,1
--- RTS: active    DTR: active    BREAK: inactive
--- CTS: active    DSR: inactive  RI: inactive  CD: inactive
--- software flow control: inactive
--- hardware flow control: inactive
--- serial input encoding: UTF-8
--- serial output encoding: UTF-8
--- EOL: CRLF
--- filters: default

--- Settings: /dev/ttyAMA0  9600,8,N,1
--- RTS: active    DTR: active    BREAK: inactive
--- CTS: active    DSR: inactive  RI: inactive  CD: inactive
--- software flow control: inactive
--- hardware flow control: inactive
--- serial input encoding: UTF-8
--- serial output encoding: UTF-8
--- EOL: CRLF
--- filters: default
```

## Appendix 5: HM-10 Test Script 

```python
import serial, time

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

print("Serial is open: " + str(ser.isOpen()))

ser.write(b'ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC')
print(str(ser.read(100)))

time.sleep(2)

ser.write(b'AT')
print(str(ser.read(100)))

ser.write(b'AT+ADDR?')
print(str(ser.read(100)))

ser.close()
```

## Appendix 6: Web Bluetooth API test

```html
<html>

<head>
    <title>Web Bluetooth</title>
</head>

<body>
    <button id="button" onclick="makeBLE()" type="button">Make BLE</button>
</body>

<script>
    function makeBLE() {
        console.log("Connecting");
        navigator.bluetooth.requestDevice({
                filters: [{
                    services: [0x484D536F6674]
                }]
            })
            .then(device => {
                // Human-readable name of the device.
                console.log(device.name);

                // Attempts to connect to remote GATT Server.
                return device.gatt.connect();
            })
            .catch(error => {
                console.log(error);
            });
    };
</script>

</html>
```

## Appendix 7: Plan Risk Assessment 

### Device communication
- **Likelihood:** Possible
- **Impact:** Medium 

Previously in the project proposal it was stated that the Web Bluetooth API would be used. I have decided to carry out additional research into the various communications technologies available to determine the most appropriate for this project. It is possible that there will be no good solution for direct device to device communication (this is intended to provide the "presence" factor of the authentication) in which case a more traditional challenge-response protocol with rotating codes displayed to students, may be appropriate. This reduces security but the ultimate aim is for this to be practical to implement. It is not envisioned this will be a "showstopper", but it would require additional research and analysis to determine an appropriate way forward. 

### Analysis of clicker system
- **Likelihood:** Unlikely
- **Impact:** Medium

This relies on the research of previous (cited) authors and it is not feasible for the investigation they carried out to be completed for this project. The intention of this section is to demonstrate a live proof of concept using their discoveries applied to the specific Royal Holloway situation - this will require developing software and a test environment. It is possible that Turning Technologies have changed the way their devices work - in this case reasonable efforts can be made to reverse engineer the devices further and research more up to date analysis. At the point firmware is needing to be dumped the benefits of including this in the report start to outweigh the time needed to complete this section, and it detracts from the rest of the project. 
This section will produce useful learnings either way, but as with all penetration testing, the exact outcome cannot be predicted in advance. 

### Frontloading functional design 
- **Likelihood:** Likely
- **Impact:**: Low

The milestones above call for the functional design to be broadly complete by the end of the first term, based on the research and proof of concept programs already developed. It is envisioned that much of the code developed during that term will be reworked and make it's way into the final release. This creates the danger that when integrating the system and building the wireframes out as a frontend panels that the architecture may need to change as the result of either changed requirements or oversights in the design process. The only mitigation to this is to ensure the code is well designed and documented, such that it can be modified as required to adapt to changing requirements. The design process should also be robust and based on the research, but it is not reasonable to expect no changes to be made further down the line. 

## Appendix 8: User Stories

### Student 

1) "As a student I want to register my attendance so I can prove I was at a lecture"
2) "As a student I want to register my attendance without distraction from the lecture content"
3) "As a student I want to be able to know my attendance has been counted"
4) "As a student I want to be able to see my attendance history" 
4) "As a student I want to register with the minimum of additional hassle"
5) "As a student I don't want to have to remember extra items to register" 

### Lecturer 

1) "As a lecturer I want to not have to think about lecture registration"
2) "As a lecturer I want to have the minimum of distractions and the minimum of fuss, in registration"
3) "As a lecturer I don't want to be involved in the registration process" 

### Administrator

1) "As an administrator I want to have all the registration data in a machine readable format"
2) "As an administrator I want to be able to easily identify students who have not reached minimum attendance levels"
3) "As an administrator I want to easily identify cases of fraud or forgery" 
4) "As an administrator I want to generate reports on attendance and export raw data" 

## Appendix 9: Test framework output

```
================================================= test session starts =================================================
platform linux -- Python 3.7.5, pytest-5.1.1, py-1.8.0, pluggy-0.12.0
rootdir: /home/crablab/Documents/RHUL/year_3/FullUnit_1920_HughWells/backend
plugins: cov-2.8.1, flask-0.15.1
collected 36 items                                                                                                    

app/tests/allocation_test.py ........                                                                           [ 22%]
app/tests/allocations_test.py ..                                                                                [ 27%]
app/tests/lecture_test.py ......                                                                                [ 44%]
app/tests/lectures_test.py ...                                                                                  [ 52%]
app/tests/user_test.py ...............                                                                          [ 94%]
app/tests/users_test.py ..                                                                                      [100%]

================================================= 36 passed in 2.01s ==================================================
```

## Appendix 10: Project Diary 

### October 21, 2019

Monday:

- Have spent the day debugging issues with serial communication
- Have written a small Python script to try sending data which isn’t working
- Discovered that I’m not actually broadcasting the hardcoded messages I thought I was (or at least they aren’t valid). I’m trying to determine why this is…

### October 28, 2019

- Finished writing up report on clicker emulation for now
- Additionally, gave up on getting the final pieces of clicker emulation to work for the moment: I will come back to it over a period of time once I’ve had a chance to consult the internet and Nuno some more, to work out what is going wrong!
- Begun researching communication methods for my proposed solution and preemptively ordered a HM-10 Bluetooth 4 module for further investigation

### November 4, 2019

- Wrote some more about clicker communication
- Got a Raspberry Pi working over Serial with Ethernet passthrough
- Determined that it’s not possible to connect to a Pi over Serial and utilize UART on the GPIO. Although the Broadcom chip support this, it is not connected in a way that allows both these Serial connections at once unless you use the Compute Module (the professional version of the Pi)
- Going to look into other options here as I want to avoid using an Arduino as I would like the networking capabilities of the Pi and the additional processing capacity. It also allows me to work with more standard cryptography libraries.

### November 4, 2019	 

- Switched from a Pi Zero to a Pi 2 and now connecting via SSH with ethernet passthrough
- UART is now working, testing to try and get communications working with the HM-10

### November 5, 2019

- I have a serial connection open, but I am not receiving data back. The board does have UART flow control pins and although I have tried the hacks (hold the enable pin low), I am still not getting any data back. Enabling hardware flow control on the Pi is possible, but involved. I have been testing with minicom and all of the Google solutions are still not enabling it.

### November 13, 2019

Yesterday:

- Worked on more issues with the UART. I think I have found a solution but it seems it requires setting a config parameter on the board itself, so I have had to purchase some additional equipment to do this.

Today:

- Researched and wrote a PoC for fingerprinting web browsers and devices
- Researched PKI and RSA vs ECDSA algorithms. Wrote a quick Adaptor class with tests to play around with a library for this. To be extended.

Current blocker is getting the Bluetooth working. Once that is done it should be fairly easy to send data end to end (he says…) 

### November 14, 2019	  

- CeDAS workshop on report writing with very useful context and helpful information about how to structure the report. Have begun laying out interim report.
- Meeting with supervisor. Discussed progress and where to concentrate work from now on. Discussed how reports are not final and feedback is really useful on work that isn’t quite complete. Structure of interim report clarified.
- Started writing up investigations into browser fingerprinting. I shall probably provide an extra POC program here for illustrative purposes.

### November 18, 2019

- Discovered an article that suggested this might well be a logic level issue on the RX pin (3.3v vs 5v) and that there are two different baud rates depending on software.
- Took notes on BLE specification stuff for a report on communication options
- Discussed project in general with Dave – the various reports and the structure the project should take, plus the specific Bluetooth issues. Dave has suggested that as per another article there could be an issue with AT commands missing a line feed/carriage return, causing the null byte issue I’m seeing

### November 20, 2019

Yesterday:

- Chatted with supervisor about clicker report. Feedback about general tone and structure of report.
- Discussed general project outline and progress to date
- Feedback on current report proposals. Agreed to add an additional report on general project ideas and outline, as without it the context of the project is somewhat confusing for an outsider.
- Communication report to be written, cryptography report to be delayed in light on the additional outline report and browser fingerprinting work.

Today:

- Implemented changes suggested in clicker report ^[https://github.com/RHUL-CS-Projects/FullUnit_1920_HughWells/pull/5]
- Working on outline report

### November 28, 2019

Earlier this week:

- Finished writing up the Outline report covering the basic system design and user stories
- Meeting with Supervisor to discuss this report, feedback and changes
- Significant research and compilation of notes on BLE specifications

Yesterday:

- Progress on Communications report theory. MIFARE attack covered and Bluetooth section complete up to part way through security features

Today:

- Finally managed to get HM-10 devices working properly. This has been delayed by waiting for hardware to arrive in dribs and drabs. An HM-10 from a different supplier and manufacturer arrived and, with no changed settings, has “magically” started working.
- I can now send data from a phone, through the HM-10 to a serial console and back again. My script to test AT commands works and various notifications are logged to the serial port when device changes take place (eg. disconnection). This is huge progress and I shall now be able to write a driver for the HM-10.
- Started work on a Web Bluetooth implementation. Have discovered that browser support is *shocking*. I currently am running experimental versions of Chromium (with flags enabled) and bluez (flags enabled) and am still encountering errors. I shall need to look further into this but it may prove unfortunatly rather fatal if I cannot find some combination of hardware that has reasonable support. Will discuss with supervisor.

### January 20, 2020

Last week:

- Wrote design report covering the proposed system design including system UML and software architecture decisions
- Started implementing webservice codebase

### January 25, 2020

- Started using GitHub Kaban board ^[https://github.com/RHUL-CS-Projects/FullUnit_1920_HughWells/projects/1]
- Setup database server (locally) and ORM
- Added design patterns to the design
- Started the final report

### February 3, 2020

Last week:

- Wrote the professional issues section of the report
- Designed database schema with constraints and dependencies

### February 4, 2020

Today:

- Making my Flask application more scalable and better structured – Started using basic Blueprints and restructured the application – Read/learnt about building basic applications in this format with SQLAlchemy and various Flask packages to help abstract functionality – Looked at unit and functional testing – Looked into scaling issues and fan-out – how do you handle databases at scale?

TODO:

- Implement full Flask factory
- Add the new ORM structure and a full class with unit tests (probably a user login page)

### February 9, 2020

- Transferred to using Blueprints and got it working!
- Using Jinja, Boostrap and What the Form have made login and signup page templates, and started on other application modules

### February 17, 2020 

Added some more pages and tried to get unit testing working. Refactored the application again to make it more scaleable and get unit testing working with the database. Focus is now going to be on getting some working code, with more basic unit testing. 

### February 18, 2020

Got the login and signup pages working. This require implementing all the logic and debugging some painful issues with flask_login. 

### March 3, 2020

Last week:

- Implemented users model with associated testing

This week so far:

- Implemented lectures and allocations to lectures
- Administrators page
- Hookins to allow allocations from the UI
- Fixed some bugs/issues

### March 10, 2020

Today:

- More report writing, including the manual
- Tried to Dockerise Arduino build environments – very fragile and didn’t work
- Looking further into WebUSB, Arduino Micro ordered

### March 18, 2020

Worked on adding more functionality for administrators and students. Merged today the functionality to allow administrators to add courses and lectures, plus students to view upcoming lectures and their next lecture.

### April 12, 2020

Finished writing up the project. Merged changes with Web USB experiments and the Dockerised Flask application 
