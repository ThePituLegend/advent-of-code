#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

input = get_input()

# ------------------ #

oxigen_can = input[:] # Oxigen candidates
col = 0
while len(oxigen_can) > 1:
    rotated = list(zip(*oxigen_can))

    crit = int(rotated[col].count(1) >= rotated[col].count(0))

    oxigen_can = list(filter(lambda n: n[col] == crit, oxigen_can))
    col += 1

co2_can = input[:] # CO2 candidates
col = 0
while len(co2_can) > 1:
    rotated = list(zip(*co2_can))

    crit = int(rotated[col].count(0) > rotated[col].count(1))

    co2_can = list(filter(lambda n: n[col] == crit, co2_can))
    col += 1
    
# https://stackoverflow.com/questions/12461361/bits-list-to-integer-in-python
oxigen = 0
for bit in oxigen_can[0]:
    oxigen = (oxigen << 1) | bit

co2 = 0
for bit in co2_can[0]:
    co2 = (co2 << 1) | bit

print(f"O2 = {oxigen}")
print(f"CO2 = {co2}")
print(f"SOLUTION <{oxigen*co2}>")