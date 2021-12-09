#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from math import prod

hmap = get_input()

# ------------------ #

def find_basin(i, j, explored):
    
    if hmap[i][j] == 9: # Border
        return

    checkpos = [(i-1, j), (i+1,j), (i, j-1), (i, j+1)] # Stencil positions
    checkpos = list(filter(lambda x: 0 <= x[0] < len(hmap) and 0 <= x[1] < len(row), checkpos)) # Drop invalid positions
    checkpos = list(filter(lambda x: x not in explored, checkpos)) # Drop explored positions

    explored.append((i, j)) # Add explored to avoid going back

    for pos in checkpos:
        find_basin(pos[0], pos[1], explored) 


sizes = []
for i, row in enumerate(hmap):
    for j, pos in enumerate(row):
        checkpos = [(i-1, j), (i+1,j), (i, j-1), (i, j+1)] # Stencil positions
        checkpos = list(filter(lambda x: 0 <= x[0] < len(hmap) and 0 <= x[1] < len(row), checkpos)) # Drop invalid positions

        if all(hmap[x[0]][x[1]] > pos for x in checkpos):
            explored = []
            find_basin(i, j, explored)
            sizes.append(len(set(explored)))

print(f"SOLUTION <{prod(sorted(sizes,  reverse=True)[:3])}>")
