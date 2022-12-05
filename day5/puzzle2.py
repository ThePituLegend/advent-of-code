#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
crates, moves = get_input()

for move in moves:
    taken = [crates[move[1]].pop() for n in range(move[0])]
    crates[move[2]].extend(taken[::-1])

for crate in crates:
    print(crate.pop(), end="")
print()