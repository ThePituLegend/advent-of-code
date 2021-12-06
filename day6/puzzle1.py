#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

timers = get_input()

# ------------------ #

for day in range(80):
    for x, fish in enumerate(timers):
        if fish == 0:
            timers.append(9)
            timers[x] = 6
        else:
            timers[x] -= 1
    
print(f"SOLUTION <{len(timers)}>")