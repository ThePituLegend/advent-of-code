#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from get_input import get_input

def get_scenic_score(map: np.ndarray, pos: tuple[int, int]) -> bool:
    x, y = pos
    target = map[x, y]

    directions = [np.flip(map[:x, y]), map[x + 1:, y], np.flip(map[x, :y]), map[x, y + 1:]] # Up, down, left, right

    score = 1
    for direction in directions:
        dir_score = 0

        for tree in direction:
            dir_score += 1
            if tree >= target:
                break

        score *= dir_score

    return score


map = get_input()

scenic_score = np.zeros_like(map)

# Iterate over all the inner trees
height, width = map.shape
for x in range(1, height - 1):
    for y in range(1, width - 1):
        scenic_score[x, y] = get_scenic_score(map, (x, y))

print(np.amax(scenic_score))