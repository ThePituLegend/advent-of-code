#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

hmap = get_input()

# ------------------ #

risk = 0
for i, row in enumerate(hmap):
    for j, pos in enumerate(row):
        checkpos = [[i-1, j], [i+1,j], [i, j-1], [i, j+1]] # Stencil positions
        checkpos = list(filter(lambda x: 0 <= x[0] < len(hmap) and 0 <= x[1] < len(row), checkpos)) # Drop invalid positions

        if all(hmap[x[0]][x[1]] > pos for x in checkpos):
            risk += 1+pos

print(f"SOLUTION <{risk}>")
