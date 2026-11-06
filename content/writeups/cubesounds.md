---
title: CubeSounds
ctf: CTFZone 2024 Quals(Jeopardy)
type: RF
difficulty: Easy
date: '2026-03-15'
category: Hardware
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/CTFZone/Cube%20Sounds
---

## Description

A strange signal was intercepted from the far side of the Moon by our Robot36 system. Perhaps this signal is the television of the future…

Who knows what is being transmitted. Maybe this is how extraterrestrial forces want to share their secrets with us?

## Overview

This challenge is composed by 10 .wav files. 

## Solution

I started opening all the files and looking at their spectrum. I saw that all of them have very similar spectrum with 4 peaks around 1200Hz, 1530Hz, 1900Hz and 2290Hz

<img src="/images/writeups/4b0fed97-6436-4c10-9384-e1e8227d1ae8.png" alt="Figure from the CubeSounds writeup" width="732" height="695" loading="lazy">

The 4 peaks and the description suggests that they are ancoded as sstv so let's try open them with qsstv
Every file produce a piece of an image and the goal is to arrange them to see the complete picture.
Opening all of them I sew that the flag is mainly written in file 5.wav so I just needed to find what file goes before and after that.
Looking at all the images I founded that the correct order is 7.wav -> 5.wav -> 3.wav
I concatenated them in a new file usin "sox 7.wav 5.wav 3.wav flag.wav" from terminal and had a look at flag.wav with qsstv

<img src="/images/writeups/715af328-6912-4d3f-adab-f219d1c275ff.png" alt="Figure from the CubeSounds writeup" width="1478" height="953" loading="lazy">

I could clearly see the flag *CTFZone{s1gn@l_dEtected!}*

## Sources

SSTV: <https://www.sigidwiki.com/wiki/Slow-Scan_Television_(SSTV>)

QSSTV: <https://github.com/ON4QZ/QSSTV>

sox: <https://hexmos.com/freedevtools/c/cmd/sox/>
