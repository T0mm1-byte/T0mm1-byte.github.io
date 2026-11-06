---
title: Debugging Interface
ctf: Hack The Box
type: Logic Signals/Protocols
difficulty: Very Easy
date: '2026-04-27'
category: hardware
author: diogt
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/HackTheBox/Debugging%20Interface
---

## Description

We accessed the embedded device's asynchronous serial debugging interface while it was operational and captured some messages that were being transmitted over it. Can you decode them?

## Overview

This challenge is composed by a .sal file.

## Solution

To start I opened the file with saleae logic. I saw that the only channel is at "1" in idle and that could be UART. The duration of a sample is 32 microseconds so the frequency is 31250 Hz. I used the saleae UART analyzer and got the flag.

<img src="/images/writeups/0df76829-b980-4c59-a873-2d84bcb3cec0.png" alt="Figure from the Debugging Interface writeup" width="591" height="762" loading="lazy">

The flag is *HTB{d38u991n9_1n732f4c35_c4n_83_f0und_1n_41m057_3v32y_3m83dd3d_d3v1c3!!52}*
