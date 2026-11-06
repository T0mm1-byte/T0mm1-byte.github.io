---
title: Communication Gateway
ctf: L3akCTF 2024(Jeopardy)
type: RF
difficulty: Easy
date: '2026-03-15'
category: hardware
author: '0x157'
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/L3akCTF/Communication%20Gateway%28radio%29
---

## Description
Something is in-front of you, and you don't even know it

## Overview
This challenge is composed by a .wav file. We have to analyze it

## Solution

I started by opening the file with Audacity and took a look at its spectrum:

<img src="/images/writeups/0c18579e-4b62-4247-b670-de59b0447f2e.png" alt="Figure from the Communication Gateway writeup" width="736" height="694" loading="lazy">

It has only two peaks: one at 1415Hz and another at 1583Hz. The difference bitween them is 168Hz that's very close to 170Hz, the standard difference used by RTTY standard. It's probably BFSK where 1583Hz is 1 and 1415Hz is 0. I could retrieve the message using minimodem but I didn't know the baudrate.
I tried all the common baudrate for RTTY like 45 and 50 but I got only garbage.
Then I remembered the description and saw that the .wav file is named "file10.wav".
What does that 10 means? Could it be the baudrate?
I tried with 10 as baudrate with "minimodem --rx -f file10.wav 10":

<img src="/images/writeups/ac38d512-f169-4705-a1a3-6cf7f4ff43f3.png" alt="Figure from the Communication Gateway writeup" width="1572" height="114" loading="lazy">

I got the flag *L3AK{s1gn4ls_0f_h0p3}*

## Sources

RTTY: <https://www.sigidwiki.com/wiki/Radio_Teletype_(RTTY>)

minimodem: <https://github.com/kamalmostafa/minimodem>
