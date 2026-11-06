---
title: Badd Circuit
ctf: FCSC 2025
type: HDL/PLC/PCB Reversing
difficulty: Easy
date: '2026-09-22'
category: hardware
author: ElyKar
repo: https://github.com/T0mm1-byte/ctf-writeups/tree/main/FCSC/Badd%20Circuit
---

## Description

Here is a logic circuit that implements an unknown function. What is the value of the 4 output bits?

The flag format is FCSC{<value>}. For example, if the value to find is 0001, the flag would be FCSC{0001}.

Note: During FCSC 2025, this challenge was limited to 3 submissions.

## Overview

This challenge is made of the picture of a digital circuit available in two formats, pdf and png.

## Solution

The request is pretty straightforward, it could be done by hand but I wrote a simple python script that emulates the circuit.

```python
input = [1, 1, 1, 0, 0, 1, 0, 0]

def XOR(x, y):
    return 1 if x != y else 0

def AND(x, y):
    return 1 if (x == y and x == 1) else 0

def OR(x, y):
    return 1 if (x + y > 0) else 0

def Struct_1(x, y, z):
    return XOR(x, XOR(y, z))

def Struct_2(x, y, z):
    return OR(AND(x, y), OR(AND(x, z), AND(y, z)))

output = list()
output.append(Struct_1(Struct_2(Struct_2(AND(input[3], input[7]), input[2], input[6]), input[1], input[5]), input[0], input[4]))
output.append(Struct_1(Struct_2(AND(input[3], input[7]), input[2], input[6]), input[1], input[5]))
output.append(Struct_1(AND(input[3], input[7]), input[2], input[6]))
output.append(XOR(input[3], input[7]))

print("FCSC{" + "".join([str(n) for n in output]) + "}")
```

The flag is *FCSC{0010}*
