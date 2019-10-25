# Investigation into Turning Point Clickers

At Royal Holloway, for the 2018 intake of first year undergraduates it was decided that due to the class size, paper registers were infeasible. The clicker systems was proposed and developed. This uses a Turning Technologies "Response Card" (Figure 1) typically used to respond to interactive questionnaires as part of a slideshow. The device communicates with a base station connected to a computer via USB (Universal Serial Bus) when a key option is pressed (eg. "1/A") and transmits the unique ID of the device and the key press. The message is acknowledged by the base station and the user is given visual affirmation on the device that their response was counted. The results are then stored in a semi-proprietary format attached to the slideshow which is decoded, processed and analysed by the department using a collection of scripts, Excel spreadsheets and custom software. 

![A Turning Technologies "Response Card"](assets/figure1.jpg)

Whilst researching the device I discovered the work of @goodspeed_travis_2010 who reverse engineered a similar, but older device. He dumped the firmware of the device allowing him to analyse the way the device operated and how packets were structured and sent. A number of important discoveries were made. 
Firstly, @goodspeed_travis_2010  writes "The Clicker is built upon a Nordic nRF24E1 chip, which combines an 8051 microcontroller with an nRF2401 radio transceiver.". The nRF2401 is a 2.4GHz, serial radio transceiver.[@nordic_semiconductor_asa_single_2004] The datasheet lists a number of potential applications including telemetry, keyless entry and home security and automation. The chip also uses what the datasheet describes as a "3-wire serial interface." - this is otherwise know as SPI (Serial Peripheral Interface) and allows easy interface with devices such as a Raspberry Pi and Arduino. 
Secondly, there is no encryption. As @goodspeed_travis_2010 writes "...it is clear that the first three bytes will be the target MAC address. From the RADIOWRCONFIG() function, it is equally clear that the three bytes at 0x1B are the receiving MAC address of the unit.". This means that the source, destination and the parameter (the button pressed) are transmitted in cleartext with the only validation being a CRC (Cyclic Redundancy Check). The message is not signed, so there is no way to verify that a message has indeed come from the advertised source. 

## Cyclic Redundancy Check 

CRC's are a method of error checking that are widely used in serial communications[@borrelli_ieee_2001]. Parity bits, which indicate whether the expected value is even or odd, have been commonly used to detect communication errors however, these suffer from two major flaws. Firstly, it is not possible for you to determine where the corruption has ocurred in a piece of data - it is (usually) not possible to repair the message and it has to be discarded and resent. Secondly, if two corruptions occur then the data may end up passing the parity check but still be invalid. Additional measures (such as length checking, strict processing validation etc.) can be included to reduce the risks of bad data being processed, but these remain significant flaws. 

There is research into error correction based on the result of CRC checksums which... {TODO AS NEED PAPER}

CRCs works using modulo arithmetic on some generated polynomials. The general formula to calculate a CRC is: 

$CRC = remainder of \left[ M(x) \times \frac{ x^n }{ G(x) } \right]$

Where `M(x)` is the sum of the message used as the coefficients in a polynomial. For example, with a message `1010`: 

$M(x) = (1 \times x^3) + (0 \times x^2) + (1 \times x^1) + (0 \times x^0)$

And `G(x)` is known as the "generating polynomial" and is generally defined by the type of CRC you are using. For CRC-16 (which is the type used for the nRF24E1) `G(x)` is defined as: 

$G(x) = (1 \times x^16) + (0 \times x^15) + (1 \times x^2) + 1$

In this particular situation, it is possible to calculate the CRC on the nRF24E1 in the ShockBurst\texttrademark configuration settings by setting the `CRC_EN` flag bit. This means the chip will calculate and append the CRC as well as strip and validate the CRC on messages received.[@nordic_semiconductor_asa_single_2004] In the @mooney_nickmooney/turning-clicker_2019 implementation, CRC is calculated on the Arduino not on the nRF24E1 due to technical issues getting this working. The CRC is instead calculated and checked using an alternative library.[@frank_frankboesing/fastcrc_2019]

## Hardware

It is possible to use any Arduino and nRF24E1 breakout board for this project - I elected to use the Arduino Nano and the cheapest nRF24E1 board I could find on eBay. The Arduino is placed on a breadboard and the nRF24E1 connected via Dupont leads to the requisite pins. 

![The wired up Arduino breadboard](assets/figure2.jpg)

As always, this can be a somewhat complex operation and it did require consultation of not only the nRF24E1's advertised pin layout[@noauthor_1/2/3/5/10_nodate] but also a setup guide for a similar, but not identical product from Sparkfun [@noauthor_nrf24l01+_nodate].

The pinout I used is as follows:

| Name | nRF24E1 | Arduino |
|------|---------|---------|
| VCC  | 2       | 3.3v    |
| GND  | 1       | GND     |
| IRQ  | 8       | GND     |
| CE   | 3       | D7      |
| CSN  | 4       | D8      |
| MOSI | 6       | D11     |
| MISO | 7       | D12     |
| SCK  | 5       | D13     |




# Acknowledgements 

Thanks to @tom_pollard_template_2016 for the front cover template which I have adapted, @marco_torchiano_how_2015 for the Pandoc table preamble and @cohen_third_2013 for the Final Year Project guide and suggested layouts. 

\pagebreak 
\onecolumn 

# Bibiography 

<!--
Due to the nature of this project, available references on the subject are limited and will be confined to more general information security concepts as well as attendance monitoring. In this report the available references are provided by those who have investigated these devices beforehand. 
-->

<div id="refs"></div>