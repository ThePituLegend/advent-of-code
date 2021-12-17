#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from itertools import repeat
from pprint import pprint
from dijkstar import Graph, find_path

input = get_input()

# ------------------ #

meta_input = [[0]*(len(input[0])*5) for _ in range(len(input)*5)]

for i in range(len(input)*5):
    for j in range(len(input[0])*5):
        val = input[i%len(input)][j%len(input[0])] + (i//len(input)) + (j//len(input[0]))
        meta_input[i][j] = ((val - 1) % 9) + 1 # 1-to-9 wraparround

graph = Graph()

for i, row in enumerate(meta_input):
    for j, pos in enumerate(row):
        checkpos = [(i-1, j), (i+1,j), (i, j-1), (i, j+1)] # Stencil positions
        checkpos = list(filter(lambda x: 0 <= x[0] < len(meta_input) and 0 <= x[1] < len(row), checkpos)) # Drop invalid positions

        for x in checkpos:
            graph.add_edge((i,j), x, meta_input[i][j])

path = find_path(graph, (0, 0), (len(meta_input)-1, len(meta_input[0])-1))


print(f"SOLUTION <{path.total_cost - meta_input[0][0] + meta_input[len(meta_input)-1][len(meta_input[0])-1]}>")  # Dijkstar take cost at leaving node.
                                                                                                            # Puzzle, at entering                                