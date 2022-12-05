#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
crates, moves = get_input()

for move in moves:
    for n in range(move[0]):
        taken = crates[move[1]].pop()
        crates[move[2]].append(taken)

for crate in crates:
    print(crate.pop(), end="")
print()