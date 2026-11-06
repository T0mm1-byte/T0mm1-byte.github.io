---
title: Firmware
ctf: GreyCTF
type: Firmware Reversing
difficulty: Very Easy
date: '2026-05-16'
category: ezpz
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/GreyCTF/Firmware
---

## Overview

This challenge is composed by a .img file that is the imagine of the firmware.

## Solution

I used "binwalk -e --term firmware.img" to see the sections and extract the squashfs file system. I then searched in it if there was a file with "grey" as string using "grep -rl "grey" ./". I found a file and when I opened it there was the the flag.

<img src="/images/writeups/9e66a13a-9b89-4986-b56c-bab10b7e9484.png" alt="Figure from the Firmware writeup" width="1798" height="233" loading="lazy">

The flag is *grey{inittab_1s_4n_1mp0rt4nt_pl4c3_t0_l00k_4t_wh3n_r3v3rs1ng_f1rmw4r3}*
