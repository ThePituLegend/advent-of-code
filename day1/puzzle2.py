#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    input_values = [int(n) for n in f.read().splitlines()]

# ------------------ #

sums = [sum(input_values[i:i+3]) for i,_ in enumerate(input_values[:-2])]

increased = 0

for i, _ in enumerate(sums):
    if sums[i] > sums[i-1]:
        increased += 1

print(f"Increased {increased} times!")