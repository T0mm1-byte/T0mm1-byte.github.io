---
title: Celestial
ctf: L3akCTF 2024(Jeopardy)
type: RF
difficulty: Easy
date: '2026-03-15'
category: hardware
author: '0x157'
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/L3akCTF/Celestial%28radio%29
---

## Description
We've received this file over the cosmic network at our headquarters. No idea what they tried to tell us, can you help ?

## Overview
This challenge is composed by a .wav file.

## Solution

I started by opening the file with Audacity and see the spectrum.

<img src="/images/writeups/0d9da82a-0e0f-4e2d-92a5-fec16e5de4bd.png" alt="Figure from the Celestial writeup" width="773" height="720" loading="lazy">

There are 4 peaks at frequences 1199Hz, 1721Hz, 1907Hz and 2256Hz. They are very close to some typical frequences used by sstv (1200Hz, 1700Hz, 1900Hz and 2300Hz). The description also suggests that it's sstv because it's used by the ISS to send images. I looked at the spectrogram to confirm it's sstv.

<img src="/images/writeups/a1519465-9cc0-4873-9309-6ab3cd0250bd.png" alt="Figure from the Celestial writeup" width="1905" height="652" loading="lazy">

Bright horizontal bands between 1400Hz and 2600Hz and a regular vertical pattern. I was fairly sure it's sstv at this point. 
I tried to open the .wav file with qsstv to decode it and see the image.

<img src="/images/writeups/b67aee82-0194-433d-b4f7-2d8d34db1da0.png" alt="Figure from the Celestial writeup" width="1914" height="1015" loading="lazy">

I could clearly see the flag *L3AK{SsTV_k1nd4_c00l!}*

## Sources

SSTV: <https://www.sigidwiki.com/wiki/Slow-Scan_Television_(SSTV>)

QSSTV: <https://github.com/ON4QZ/QSSTV>
