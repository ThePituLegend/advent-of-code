#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from statistics import median

crabs = get_input()

# ------------------ #

align_pos = int(median(crabs))
print(f"With align pos {align_pos}")

fuel = 0
for crab in crabs:
    cost = abs(crab-align_pos)
    print(f"Move from {crab} to {align_pos}: {cost} fuel")
    fuel += cost

print(f"SOLUTION <{fuel}>")