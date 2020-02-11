## Appendix 1

```html
<html>

<head>
    <title>Device Fingerprinting</title>
    <script type="text/javascript" src="fingerprint2.js"></script>
    <script src="client.min.js"></script>
</head>

<body>
    <h1>Your Fingerprint2 is: <code id="fp1"></code></h1>
    <h1>Your ClientJS fingerprint is: <code id="fp2"></code></h1>
</body>

</html>
```

## Appendix 2

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
