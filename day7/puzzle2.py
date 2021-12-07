#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from statistics import median

crabs = get_input()

# ------------------ #

fuels = []
for align_pos in range(min(crabs), max(crabs)+1):
    fuel = 0
    for crab in crabs:
        cost = sum(range(1, abs(crab-align_pos)+1))
        #print(f"Move from {crab} to {align_pos}: {cost} fuel")
        fuel += cost
    
    #print(f"Total cost of pos {align_pos} => {fuel}")
    #print()
    fuels.append(fuel)

print(f"SOLUTION <{min(fuels)}>")