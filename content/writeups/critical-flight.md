---
title: Critical Flight
ctf: Hack The Box
type: HDL/PLC/PCB Reversing
difficulty: Very Easy
date: '2026-04-27'
category: hardware
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/HackTheBox/Critical%20Flight
---

## Description

Your team has assigned you to a mission to investigate the production files of Printed Circuit Boards for irregularities. This is in response to the deployment of nonfunctional DIY drones that keep falling out of the sky. The team had used a slightly modified version of an open-source flight controller in order to save time, but it appears that someone had sabotaged the design before production. Can you help identify any suspicious alterations made to the boards?

## Overview

This challenge is composed by thirteen .gbr files

## Solution

I opened the files using gerbv and found the flag written on the copper.

<img src="/images/writeups/738b7d7e-d09b-4871-b5bc-d7a3804deb37.png" alt="Figure from the Critical Flight writeup" width="1451" height="847" loading="lazy">
<img src="/images/writeups/1dad403e-e14a-4ef2-a683-47cd341c585d.png" alt="Figure from the Critical Flight writeup" width="1449" height="843" loading="lazy">

The flag is *HTB{533_7h3_1nn32_w02k1n95_0f_313c720n1c5#$@}*
