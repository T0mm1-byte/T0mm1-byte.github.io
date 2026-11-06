---
title: Sanity
ctf: TORX Finals 2026
type: Logic Signals/Protocols
difficulty: Easy
date: '2026-09-29'
category: hardware
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/TORX/Sanity
---

## Description

Sanity check, if everything it is ok on the board you will get the flag. (It requires a hardware modification, talk to the organizers when you are sure you've understood what to do)

## Overview

This was the first of six hardware challenges available in place at TORX finals 2026. They gave us a custom board with a STM32F103C8T6, a FT232H USB and a Saleae clone. The challenges were all stored in the board and could be solved in any order besides the first one, Sanity.

<img src="/images/writeups/873746eb-74cc-4356-9320-64cfe065d524.jpeg" alt="Figure from the Sanity writeup" width="1594" height="2560" loading="lazy">

## Solution

The first thing I did was trying to communicate with the board using the ft232 but it just seemed impossible. I sampled each pin using the logic analyzer but they were all either constantly high or constantly low. I saw two sets of four pins each where one of them was constantly high, one was constatntly low and the other two were disconnected from the board. I thought they were UART pins so I asked the hosts to solder a resistor to connect them. It was correct. Unfortunately I didn't take a photo of the board before the modification so here's the final result:

<img src="/images/writeups/30f7232d-e4ef-4fdc-a687-9a40ac1b862a.jpeg" alt="Figure from the Sanity writeup" width="2560" height="2501" loading="lazy">

I connected the board to my pc and tried to open a shell with "picocom -b 115200 /dev/ttyUSB0".

<img src="/images/writeups/2853d35f-4bf8-40f2-a6e7-9fc237ec3cc1.jpeg" alt="Figure from the Sanity writeup" width="2069" height="2560" loading="lazy">

It worked. The baudrate was a guess, the most common ones are 115200 and 9600. If they would've failed I would've just sampled the TX pin with the logic analyzer to find the baudrate. Now I had a shell and typing "help" took me to a menu with four commands: list, to list the six available challenges, info n (with n the challenge number), to print the description, load n (with n the challenge number), to prepare a challange, and jump, to start the challenge prepared with the last load.
I typed "load 0" to prepare Sanity and then "jump" to execute it. 

<img src="/images/writeups/9f07659c-08dc-4038-b73f-a117dacbca91.png" alt="Figure from the Sanity writeup" width="1819" height="227" loading="lazy">

The board printed a bunch of stuff and then gave me the flag *TORX{n0w_th4t_3v3ryt1ng_w0rk5_h4v3_fun}*
