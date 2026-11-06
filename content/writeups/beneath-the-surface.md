---
title: Beneath the Surface
ctf: L3akCTF 2025(jeopardy)
type: RF
difficulty: Medium
date: '2026-03-15'
category: hardware
author: Suvoni
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/L3akCTF/Beneath%20the%20Surface
---

## Description

On the surface, this signal is nothing but meaningless noise — a mere whisper of the wind. But dive deeper into this transmission, and a storm begins to take shape, with gray skies gathering on the horizon. Can you navigate through the static and uncover what lurks beneath the surface of the wav — before it’s too late?

## Overview

This challenge is composed by a .wav file.

## Solution

I started by opening the file with Audacity to look at the spectrum.

<img src="/images/writeups/2360ba74-23de-49df-a0f2-7a6b0535215a.png" alt="Figure from the Beneath the Surface writeup" width="729" height="666" loading="lazy">

There are 4 peaks at 299Hz, 449Hz, 1449Hz and 2279Hz.
Looking at the spectrogram I sea that only 1449Hz and 2279Hz are really part of the signal

<img src="/images/writeups/15958e55-ad37-411b-80cd-8824bb8c4149.png" alt="Figure from the Beneath the Surface writeup" width="1905" height="426" loading="lazy">

I used "strings beneath_the_surface.wav > metadata.txt" to see the metadata.

<img src="/images/writeups/c015f354-1067-48f1-9b35-14145305a527.png" alt="Figure from the Beneath the Surface writeup" width="368" height="225" loading="lazy">

It's wefax. It makes sense because the peaks are very close to the usual frequencies used by wefax (1500Hz and 2300Hz). I used fldigi to recover the image.

<img src="/images/writeups/91f89c5c-f5e4-44bf-a346-17750c1670d6.png" alt="Figure from the Beneath the Surface writeup" width="1049" height="637" loading="lazy">

I could clearly see the flag *L3AK{R4diOF4X_1S_G00d_4_ImAG3_Tr4nsM1sSiON}*

## Sources

WEFAX: <https://www.sigidwiki.com/wiki/WEFAX>

fldigi: <https://www.w1hkj.org/FldigiHelp/>
