---
title: Sal
ctf: BYUCTF 2024(Jeopardy)
type: Logic Signals/Protocols
difficulty: Medium
date: '2026-04-04'
category: IoT
author: Legoclones
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/BYUCTF/Sal
---

## Description

A few friends and I recently hacked into a consumer-grade home router. Our first goal was to obtain the firmware. To do that, we hooked up a SOIC-8 clip to the external flash memory chip, connected a Saleae Logic Pro 8 logic analyzer, and captured data using Logic 2 as we booted up the IoT device. The external flash memory chip was Winbond 25Q128JVSQ.


What's the md5sum of /etc/passwd?


Flag format - byuctf{hash}

## Overview

The challenge is composed by seven .bin files and a meta.json file. They are the results of an extraction from a .sal file where each of the .bin contains the data of one channel and the .json file contains the metadata. The goal is to understand the way the communiction works to build the firmware and get the hash of passwd.

## Solution

The first thing I did was to read the datasheet of the flash memory chip.

<img src="/images/writeups/b7e4053b-8a63-42ba-8132-27f14e7b54bc.png" alt="Figure from the Sal writeup" width="831" height="292" loading="lazy">
<img src="/images/writeups/9920a87d-00d5-4b0f-9b4d-0b4fdb6da498.png" alt="Figure from the Sal writeup" width="867" height="832" loading="lazy">
<img src="/images/writeups/9c5efa6f-9c76-445d-aea6-fce76215d353.png" alt="Figure from the Sal writeup" width="846" height="779" loading="lazy">

There are eight signals: /CS, DO(MISO), /WP, GND, DI(MOSI), CLK, /HOLD e VCC. I recomposed the original .sal file using the command "zip -0 capture.sal meta.json digital-0.bin ... digital-6.bin" and opened it in Saleae Logic to see the waves. Knowing how SPI works it was pretty easy to recognize channel 1 as CLK, channel 2 as /CS, channel 3 as DI and channel 4 as DO. Saleae offers an embedded SPI Analyzer so I used it to map the protocol.

<img src="/images/writeups/259f2072-a71d-4af5-aec4-a68ef9dd7fdd.png" alt="Figure from the Sal writeup" width="659" height="796" loading="lazy">

I then used the extension SPI Flash to translate the bytes to instructions.

<img src="/images/writeups/68554848-c0d1-4a4a-bb05-13d09d5615b7.png" alt="Figure from the Sal writeup" width="1482" height="965" loading="lazy">

They are almost all read data instructions (0x03) with some read status instructions (0x05) near the end. Each instruction is composed like this: the first byte of MOSI is the opcode (only 0x03 and 0x05 in this case), the next three bytes of MOSI are the address to read. Starting from the fifth byte of MISO there are the data bytes (the firmware in this case). There are usually four byte of data per instructions but it can vary, for example in some instruction there is only one byte of data. Knowing that I exported the table as a .csv file and wrote a script to read from the .csv and build the firmware. The flash memory is 16MB so I inizialized the firmware as 0x10000000 0xFF. This way I avoided problems like reading more times the same bytes and I had already set the unutilized bytes as 0xFF that is the standard.

```python
import csv

MOSI = list()
MISO = list()

with open('SPI_results.csv', mode='r', encoding='utf-8') as file:
    content = csv.reader(file, delimiter=',')
    mosi = b""
    miso = b""

    for row in content:
        if row[0] == "SPI" and row[3] != "0.000000004":
            mosi += bytes([int(row[4], 16)])
            miso += bytes([int(row[5], 16)])
        else:
            if mosi != b"" and miso != b"":
                MOSI.append(mosi)
                MISO.append(miso)
                mosi = b""
                miso = b""


firmware = bytearray(b'\xff'*0x1000000)

with open("firmware.bin", "wb") as firm:

    for i in range(len(MOSI)):

        if MOSI[i][0] != 0x03:
            print(f"Problem, found a different opcodes in position {i}: {MOSI[i][0]}")
            continue

        addr = int.from_bytes(MOSI[i][1:4], byteorder="big")
        data = MISO[i][4:]
        firmware[addr:addr+len(data)] = data

    firm.write(firmware)
```

The next thing I did was to run "binwalk --term firmware.bin" to see if the script did a good job.

<img src="/images/writeups/f21fafb6-ef21-44a4-bb1e-ed01a1dca47d.png" alt="Figure from the Sal writeup" width="1899" height="204" loading="lazy">

All seemed fine so I extracted all using "binwalk -e firmware.bin" and then I found the hash using "md5sum _firmware.bin.extracted/squashfs-root/etc/passwd".

<img src="/images/writeups/89d9efa3-a4ea-4786-b51c-35a0dfcd8f71.png" alt="Figure from the Sal writeup" width="496" height="23" loading="lazy">

So the flag is *byuctf{c8ef3ad94c6eb97f4fa94a0f0ed33980}*

## Sources

Winbond 25Q128JVSQ Datasheet: <https://www.mouser.com/datasheet/2/949/w25q128jv_revf_03272018_plus-1489608.pdf>

SPI Analyzer guide: <https://www.saleae.com/support/protocol-analyzers/analyzer-user-guides/using-spi>

SPI Flash extension: <https://github.com/adafruit/Logic2-SPIFlash>

binwalk tutorial: <https://sergioprado.blog/reverse-engineering-router-firmware-with-binwalk/>
