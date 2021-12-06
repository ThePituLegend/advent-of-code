#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

lines, corner = get_input()

# ------------------ #
vents = [[0 for _ in range(corner[0]+1)] for _ in range(corner[1]+1)]

for line in lines:
    ori = int(line[0][0] == line[1][0]) # 0 / 1 <orientation axis>
    start = min(line[0][ori], line[1][ori])
    stop = max(line[0][ori], line[1][ori]) + 1
    mov_range = range(start, stop)
    fix = line[0][not ori] # <fixed axis>
    
    if line[0][0] == line[1][0]: # V
        for y in mov_range:
            vents[y][fix] += 1

    elif line[0][1] == line[1][1]: # H
        for x in mov_range:
            vents[fix][x] += 1
    else:
        lower = 0 if line[0][1] > line[1][1] else 1 # Lowest y
        upper = int(not lower)

        start_x = min(line[0][0], line[1][0])
        stop_x = max(line[0][0], line[1][0]) + 1

        direction = 1 if line[lower][0] > line[upper][0] else -1

        y = line[upper][1] if direction == 1 else line[lower][1]
        
        for x in range(start_x, stop_x):
            vents[y][x] += 1
            y += direction        
    
cross = len([val for row in vents for val in row if val >= 2])
print(f"SOLUTION <{cross}>")
 