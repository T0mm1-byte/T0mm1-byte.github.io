---
title: Strange Transmission
ctf: L3akCTF 2025(Jeopardy)
type: RF
difficulty: Easy
date: '2026-03-15'
category: hardware
author: Suvoni
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/L3akCTF/Strange%20Transmission%28beginner%29
---

## Description

I received this strange transmission and I'm not sure what to make of it! Weird beeps, static noise, then silence. Can you help me figure out what it all means?

## Overview

This challenge is composed by a .wav file.

## Solution

I started by analyzing the spectrum with Audacity.
I saw one peak at 1003Hz. Using just one frequence it may be morse code:

<img src="/images/writeups/f4708fd9-9d9e-4dce-aae3-029e27f5fffc.png" alt="Figure from the Strange Transmission writeup" width="751" height="705" loading="lazy">

Then I looked at the spectrogram. There are two regions: the first one is just a repeated peak while the second, at the end of the file, looks a little weird

<img src="/images/writeups/9347f4a2-aff9-4084-98e8-22b2610544b5.png" alt="Figure from the Strange Transmission writeup" width="1900" height="571" loading="lazy">

I zoomed int the second area saw the final part of the flag.

<img src="/images/writeups/4d0ebc95-4441-4f2d-9fe3-5fff4c73a502.png" alt="Figure from the Strange Transmission writeup" width="1202" height="255" loading="lazy">

I tried to decode the first region as morse code.

<img src="/images/writeups/c5726337-42e1-4558-b24a-fb950c852413.png" alt="Figure from the Strange Transmission writeup" width="1273" height="762" loading="lazy">

It is morse code and the message is "oh wow you found our secret morse code audio, well done, here is the first half of the flag: L3AK{welc0m3_t0_th3_h4rdw4r3_rf_".

I just had to concatenate the two flag pieces and got *L3AK{welc0m3_t0_th3_h4rdw4r3_rf_c4teg0ry_w3_h0p3_you_h4ve_fun!}*

## Sources

Morse decoder: <https://morsecode.world/international/decoder/audio-decoder-adaptive.html>
