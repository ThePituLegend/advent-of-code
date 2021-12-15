#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from get_input import get_input

polymer, rules = get_input()

# ------------------ #
pairs = defaultdict(int, {polymer[i:i+2]: polymer.count(polymer[i:i+2]) for i in range(len(polymer)-1)})
counts = defaultdict(int, {x: polymer.count(x) for x in set(polymer)})

for step in range(40):
	new_pairs = defaultdict(int)
	for p, n in pairs.items():
		p1 = p[0] + rules[p]
		p2 = rules[p] + p[1]

		new_pairs[p1] += n
		new_pairs[p2] += n

		counts[rules[p]] += n

	pairs = new_pairs

print(f"SOLUTION <{max(counts.values()) - min(counts.values())}>")