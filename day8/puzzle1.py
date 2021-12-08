#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
input = get_input()

# ------------------ #

LUT = { # Num. of seg: rendered number
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

unique = 0
for line in input:
    patterns, output = line

    for digit_len in map(lambda x: len(x), output):
        if digit_len in LUT:
            unique += 1

print(f"SOLUTION <{unique}>")
