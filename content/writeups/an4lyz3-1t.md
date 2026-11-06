---
title: An4lyz3_1t
ctf: Asian Cyber Security Challenge 2024(Jeopardy)
type: Logic Signals/Protocols
difficulty: Very Easy
date: '2026-03-09'
category: hardware
author: Chainfire73
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/ACSC/An4lyz3_1t
---

## Description

Our surveillance team has managed to tap into a secret serial communication and capture a digital signal using a Salae logic analyzer.
Your objective is is to decode the signal and uncover the hidden message.

## Overview

This challenge is composed by a .sal file. 

## Solution

Let's open the .sal file using Logic.
<img src="/images/writeups/7fdca621-30f5-451f-ac8a-3466050a4807.png" alt="Figure from the An4lyz3_1t writeup" width="1832" height="272" loading="lazy">

There is a single channel signal and the duration of each high and low is a multiple of 17.375 microseconds. This is a common frequency for UART using 57600 as baudrate. It's probably UART also because the signal is high in idle and goes to low before sending 8 bits. I saw that the bits sent are 9 so there's also a parity bit. I tried to use the Async Serial analyzer to see if the idea is correct.

<img src="/images/writeups/00619c8d-45f7-4495-a6d2-d5913aa085cb.png" alt="Figure from the An4lyz3_1t writeup" width="897" height="796" loading="lazy">
<img src="/images/writeups/8436dbf9-6028-4b53-b14b-6b51dd30cd59.png" alt="Figure from the An4lyz3_1t writeup" width="383" height="867" loading="lazy">

I got the flag: *ACSC{b4by4n4lyz3r_548e8c80e}*

## Sources

Async Serial analyzer: <https://www.saleae.com/support/protocol-analyzers/analyzer-user-guides/using-async-serial>
