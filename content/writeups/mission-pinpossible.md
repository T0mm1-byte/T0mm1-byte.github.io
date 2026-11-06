---
title: Mission Pinpossible
ctf: Hack The Box
type: Logic Signals/Protocols
difficulty: Medium
date: '2026-06-02'
category: hardware
author: diogt
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/HackTheBox/Mission%20Pinpossible
---

## Description

Our field agent cannot access the enemy base due to the password-protected internal gates, but observed that the password seemed to be partially displayed as it was typed into the security keypad. Thanks to an audacious mission, we were able to implant an embedded device into the wiring for the keypad's monitor, and intercepted some data. Your mission is to recover the password from the collected data.

## Overview

This challenge is composed by a .logicdata file and a .jpeg that shows a led display with 2x16 regions of 5x8 pixels and a PCF8574T I2C extender.

## Solution

I started reading the datasheet of both the display and the extender. I found out that the display as a map where each char rapresentation is linked to its ascii encoding (for example, if I want to write an 'A' in the display I have to send a 0x41 to it) but the particular thing is how it takes the bytes. 

<img src="/images/writeups/f230b641-5ed4-4ea4-a4d5-5d37b763555c.png" alt="Figure from the Mission Pinpossible writeup" width="849" height="894" loading="lazy">

<img src="/images/writeups/25e7c612-9a08-43b6-b941-904a935f924c.png" alt="Figure from the Mission Pinpossible writeup" width="899" height="736" loading="lazy">

<img src="/images/writeups/e1a2155d-70ed-4843-8dcd-6c99af03a27c.png" alt="Figure from the Mission Pinpossible writeup" width="1442" height="771" loading="lazy">

<img src="/images/writeups/e8b14cb3-a827-4dd7-97bc-ea4ad1e47bad.png" alt="Figure from the Mission Pinpossible writeup" width="1412" height="647" loading="lazy">

The extender has 8 GPIO pins that are used to write the data but the four least significant of them are used as control signals and not to transmit data. That means that to write a byte the extender must send two bytes and in each of them the four most significant bits are the nibble of the real byte. For example, to send "0x41" the extender will send "0x4X" and "0x1X". Actually to transmit a single nibble it's necessary to transmit three byte: "0xX9", "0xXD" and "0xX9". The bit that changes between 0xD and 0x9 is the EN bit and it should go from low to high to low again. The four lower bits are RS = 1 (the extender is sending a data, not a command), RW = 0 (write operation), EN (0 and 1 as explained before) and BL = 1 (4 bit mode, each byte transmitted contains 4 bit of data). This explain why 0x9 and 0xD as lower nibble in each transmitted byte. So what I expected was that, for example, the sequence 0x49 0x4D 0x49 0x19 0x1D 0x19 = "A". I opened the .logicfile with saleae 1.x.y (the old version) and applied its embedded I2C analyzer to see the bytes.

<img src="/images/writeups/966db3d2-a126-47e6-a0a8-a227e2e27e80.png" alt="Figure from the Mission Pinpossible writeup" width="1608" height="549" loading="lazy">

I saw that each block of transmission is "Enter Password" followed by a sequence of "0x2A" and an arbitrary last byte. The first two last bytes were "H" and "T" so I was pretty sure that I should just recover the last bytes of each block and so I did. Honestly I had no idea about how to script it so I just did it by hand.

I got the flag *HTB{84d_d3519n_c4n_134d_70_134k5!d@}*

## Sources

I2C extender: <https://www.nxp.com/docs/en/data-sheet/PCF8574_PCF8574A.pdf>

Display: <https://cdn.sparkfun.com/assets/9/5/f/7/b/HD44780.pdf>
