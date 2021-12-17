#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from dijkstar import Graph, find_path

input = get_input()

# ------------------ #

graph = Graph()

for i, row in enumerate(input):
    for j, pos in enumerate(row):
        checkpos = [(i-1, j), (i+1,j), (i, j-1), (i, j+1)] # Stencil positions
        checkpos = list(filter(lambda x: 0 <= x[0] < len(input) and 0 <= x[1] < len(row), checkpos)) # Drop invalid positions

        for x in checkpos:
            graph.add_edge((i,j), x, input[i][j])

path = find_path(graph, (0, 0), (len(input)-1, len(input[0])-1))

print(f"SOLUTION <{path.total_cost - input[0][0] + input[-1][-1]}>") # Dijkstar take cost at leaving node.
                                                                                            # Puzzle, at entering