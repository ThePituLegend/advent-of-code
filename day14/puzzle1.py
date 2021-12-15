#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from get_input import get_input

polymer, rules = get_input()

# ------------------ #

for step in range(10):
	new_polimer = ""
	for i, _ in enumerate(polymer[:-1]):
		new_polimer += polymer[i]
		new_polimer += rules[polymer[i:i+2]]
	new_polimer += polymer[-1]
	polymer = new_polimer

counts = Counter(polymer)
print(f"SOLUTION <{max(counts.values()) - min(counts.values())}>")