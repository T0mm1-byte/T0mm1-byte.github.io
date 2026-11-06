---
title: Dumb Internet Of Things
ctf: TyphoonCon CTF 2023(Jeopardy)
type: Firmware Reversing
difficulty: Medium
date: '2026-05-18'
category: rev
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/TyphoonConCTF/DumbInternetOfThings
---

## Description

Some employee from the engineering team at DumbIOT inc. got drunk and left the prototype of some new sensor device around in our bar.

Here's the firmware dump, can you try to get anything from it?

Flag structure: S3D{...}

## Overview

The challenge is composed by a .bin file, the dump of a firmware.

## Solution

The first thing I did was using "binwalk -e --term dump.bin" to extract the squashfs file system. Searching for some custom binaries in /usr/bin I foundrunProcess. I opened it in IDA and started analyzing it. The flow is pretty simple: it uses the mbedtls functions to establish an ssl connection to a server, sends a request to it, attends a response and then ends. To get the flag I tried to do the same. I identified when the device sends the request:

<img src="/images/writeups/9a12e81e-35e0-48cb-a4e8-671e6ef5de4f.png" alt="Figure from the Dumb Internet Of Things writeup" width="688" height="568" loading="lazy">

<img src="/images/writeups/b0147d38-74f1-4969-923c-91b5d01ddee4.png" alt="Figure from the Dumb Internet Of Things writeup" width="538" height="445" loading="lazy">

and I searched for each element. The request template:

<img src="/images/writeups/3a76fd4a-844b-4861-bd5f-c1e842965e36.png" alt="Figure from the Dumb Internet Of Things writeup" width="971" height="360" loading="lazy">

the host:

<img src="/images/writeups/feee62e6-c761-404d-a19b-3e3497fcdbc9.png" alt="Figure from the Dumb Internet Of Things writeup" width="963" height="164" loading="lazy">

The token:

<img src="/images/writeups/728c39a9-86ee-4ab2-99e5-e964c46ec79a.png" alt="Figure from the Dumb Internet Of Things writeup" width="883" height="244" loading="lazy">

<img src="/images/writeups/0f403fff-801e-4660-900d-9250c522a47e.png" alt="Figure from the Dumb Internet Of Things writeup" width="439" height="307" loading="lazy">

The payload and the payload size:

<img src="/images/writeups/e2c27ed7-c7ae-4b4e-b44c-79c3a9cd7d4f.png" alt="Figure from the Dumb Internet Of Things writeup" width="786" height="349" loading="lazy">

<img src="/images/writeups/3284387f-e6df-4de9-adbe-2e22caa44717.png" alt="Figure from the Dumb Internet Of Things writeup" width="858" height="104" loading="lazy">

Then I did the same request and got the flag *S3D{They_d0nt_mak3_like_th3y_u5ed_to}*

## Sources

mbedtls info: <https://sourcevu.sysprogs.com/stm32/Libraries/mbedTLS/symbols/>
