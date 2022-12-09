#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from get_input import get_input

def check_visibility(map: np.ndarray, pos: tuple[int, int]) -> bool:
    x, y = pos
    target = map[x, y]

    directions = [map[:x, y], map[x + 1:, y], map[x, :y], map[x, y + 1:]] # Up, down, left, right

    return np.any([target not in direction and max(direction) < target for direction in directions])


map = get_input()

height, width = map.shape
visible = ((width * 2) + (height * 2)) - 4 # Corners overlap

# Iterate over all the inner trees
for x in range(1, height - 1):
    for y in range(1, width - 1):
        visible += check_visibility(map, (x, y))

print(visible)