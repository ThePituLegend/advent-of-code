#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from get_input import get_input

dots, folds = get_input("example.txt")

# ------------------ #

paper = defaultdict(bool)
paper.update({dot: True for dot in dots})

size = [max(dots, key=lambda x: x[1])[1] + 1, max(dots, key=lambda x: x[0])[0] + 1]

for fold in folds:
    if fold[0] == "y": # Up fold
        for x in range(size[0]):
            for i in range(fold[1]):
                #print((x, i), "<->", (x, size[0]-(i+1)), "=>", paper[(-(i+1), x)])
                paper[(x, i)] |= paper[(x, size[0]-(i+1))]
                del paper[(x, size[0]-(i+1))]
        
        size[0] = fold[1]

    else: # Left fold
        for i in range(fold[1]):
            for y in range(size[1]):
                #print((i, y), "<->", (size[1]-(i+1), y), "=>", paper[(size[1]-(i+1), y)])
                paper[(i, y)] |= paper[(size[1]-(i+1), y)]
                del paper[(size[1]-(i+1), y)]

        size[1] = fold[1]

for x in range(size[0]):
    for y in range(size[1]):
        print("█" if paper[(y,x)] else " ", end="")
    print()
