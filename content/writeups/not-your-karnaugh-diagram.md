---
title: Not Your Karnaugh Diagram
ctf: QnQSecCTF 2025
type: HDL/PLC/PCB Reversing
difficulty: Very Easy
date: '2026-06-02'
category: hardware
author: Labyad
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/QnQSecCTF/NotYourKarnaughDiagram
---

## Description

Give the proper function as a binary string where the bottom line is the MSB of the string and the top line is the LSB, challenge files linkedin below:

flag format: QnQSec{1111 1111 1111 1111} (binary)

## Overview

This challenge is composed by a .pdf file.

## Solution

In the pdf there are a Karnaugh Diagram and a Truth Table to complete. And that's it, this is the whole challenge. 

<img src="/images/writeups/79060b68-1538-44f3-8733-984ec971a051.png" alt="Figure from the Not Your Karnaugh Diagram writeup" width="835" height="861" loading="lazy">

I completed the table and got the flag *QnQSec{0110 0110 0001 0001}*
