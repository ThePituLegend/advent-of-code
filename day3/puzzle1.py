#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from statistics import mode
from get_input import get_input

input = get_input()

# ------------------ #

rotated = list(zip(*input))
gamma_bits = [mode(col) for col in rotated]

# https://stackoverflow.com/questions/12461361/bits-list-to-integer-in-python
gamma = 0
epsilon = 0
for bit in gamma_bits:
    gamma = (gamma << 1) | bit
    epsilon = (epsilon << 1) | ((bit+1) % 2) # Epsilon = ~Gamma, but Python signedness doesn't allow that

print(f"γ = {gamma}")
print(f"ε = {epsilon}")
print(f"SOLUTION <{gamma*epsilon}>")