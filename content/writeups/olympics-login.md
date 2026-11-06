---
title: Olympics Login
ctf: Iran Tech Olympics CTF 2025(Jeopardy)
type: Firmware Reversing
difficulty: Medium
date: '2026-07-26'
category: hardware
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/IranTechOlympicsCTF/OlympicsLogin
---

## Description

We're facing another Olympic login challenge for an IoT device. If you can log in correctly, the flag will be displayed.

## Overview

This challenge is composed by a .bin file that is a Cortex-M firmware.

## Solution

*Being a Bare-Metal firmware, it haven't got debug symbols. In the photos you will see the functions' names given by me, in the original they were sub_[address]*

Using the "file" command I saw the binary has the Flash at 0x8000000 and the RAM at 0x20000000 so it's clearly an STM. I opened it in IDA and went to the reset handler.

<img src="/images/writeups/0083ca20-f5f1-4746-82d8-90100dd230fd.png" alt="Figure from the Olympics Login writeup" width="767" height="675" loading="lazy">

Cortex-M standard logic: the reset handler calls SystemInit to setup some stuff, copies bytes from Flash to RAM (.data), fills a part of RAM with 0s (.bss), calls __libc_init_array and finally calls main. Nothing strange since here so I checked the main.

<img src="/images/writeups/0040eb1a-3cf4-4b74-aa17-e7ff5d9f506d.png" alt="Figure from the Olympics Login writeup" width="676" height="450" loading="lazy">

This isn't a classic STM32 main, it looks like an arduino code with a rsetup and an infinite loop. My conclusion was that I was looking at a STM32duino such as a blue pill. initVariant is labeled "weak" since it's not useful for most boards (like this one) and the linker replaced the BL instruction to it with a NOP.W. serialEventRun is useless as well since there isn't any serial Event defined. I focused on setup() and loop().

<img src="/images/writeups/d759d145-3004-4587-9de1-b31baa2b13c3.png" alt="Figure from the Olympics Login writeup" width="287" height="357" loading="lazy">

Setup calls a function with three parameters and it' clearly an inizialization of a serial communication sinche these parameters are a RAM address (that I called serial_conn), 9600 (the baudrate) and 6 (UART 8N1). So I knew loop() would expect some type of communication and from the description it's clear it will be some type of authentication. Looking at loop() I found this theory correct.

<img src="/images/writeups/1285c043-bba7-4aae-8e98-474c8c54cf93.png" alt="Figure from the Olympics Login writeup" width="707" height="657" loading="lazy">

I saw two functions. The first one it's used to receive chars and buffer them so I called it receive_line. Nothing strange with it.

<img src="/images/writeups/a53fb629-1582-4f54-8436-d4d425c51310.png" alt="Figure from the Olympics Login writeup" width="697" height="690" loading="lazy">

The second one is more interesting since it's a simple two-state machine that takes two inputs (username and password as I would've discovered later) and then calls a function to validate them. 

<img src="/images/writeups/431a02df-cbf4-4311-a360-aa962ee7d209.png" alt="Figure from the Olympics Login writeup" width="356" height="400" loading="lazy">

The function I called inputValidation contains the true logic of the challenge. There is a function to validate username and password (as it's written in the error messages) that are the first part of the flag, and then there are some functions to calcolate v4 that is the last part of the flag.

<img src="/images/writeups/95392e47-008d-4c8f-8c5a-d38892018694.png" alt="Figure from the Olympics Login writeup" width="837" height="602" loading="lazy">

The function that checks username and password is the same but with different parameters and it's extremely simple to reverse since it's just a xor.

<img src="/images/writeups/3a80d03e-12fc-462f-a6b2-dd3ee85441ac.png" alt="Figure from the Olympics Login writeup" width="1012" height="268" loading="lazy">

The eight functions to calculate v4 can be divided in two blocks of 4 functions that have the look of hashing function: Init, Update, Final and a conversion from hex to string. Looking at the Init functions of the two blocks I saw, from their costants, they are two different hashes: SHA-256 and MD5. So the last part of the flag is MD5(SHA256(x)) where x is the string conversion of some bytes in the Flash.

<img src="/images/writeups/3ec00300-061c-44a7-bdb4-cb4c56db75d2.png" alt="Figure from the Olympics Login writeup" width="388" height="305" loading="lazy">

<img src="/images/writeups/36adb373-1448-48eb-9f2d-0ef0cdbf1cab.png" alt="Figure from the Olympics Login writeup" width="383" height="222" loading="lazy">

At this point I just coded a script to get the flag.

```python
import hashlib

first_buff = [0x70, 0x11, 0xEB, 0x34, 0x19, 0x1B, 0x18, 0xCC]
second_buff = [0x1E, 0x22, 0x9F, 0x75, 0x7D, 0x76, 0x39, 0xA2]

username_buff = [x ^ y for x, y in zip(first_buff, second_buff)]
username = "".join([chr(c) for c in username_buff])

third_buff = [0x02, 0x03, 0x1A, 0x06, 0x3B, 0x01, 0x10, 0x18, 0x5D, 0x6C, 0x2B, 0x31,
              0x24, 0x1E, 0x14, 0x19, 0x5E, 0x41, 0x30, 0x32, 0x45, 0x4C, 0x00, 0x51]
user_3 = username * 3
user_buff = [ord(c) for c in user_3]

password_buff = [x ^ y for x, y in zip(third_buff, user_buff)]
password = "".join([chr(c) for c in password_buff])

msg = b"1e229f757d7639a2"
d1  = hashlib.sha256(msg).hexdigest()          
v4  = hashlib.md5(d1.encode()).hexdigest() 

print("flag: ASIS{" + username + "_" + password + "_" + v4 + "!}")
```

I got the flag *ASIS{n3tAdm!n_l0nG_l1v3__p@s5w0rDs!!!?_35390bed4dc7055a9d26f610c454ab2d!}*
