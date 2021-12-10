#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from statistics import median

input = get_input()

# ------------------ #

push_char = ["{", "(", "[", "<"]
pop_char = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

scores = {
    "{": 3,
    "(": 1,
    "[": 2,
    "<": 4
}

total_scores = []
for line in input:
    stack = []
    local_score = 0

    for char in line:
        if char in push_char:
            stack.append(char)
        else:
            opening = stack.pop()
            if char != pop_char[opening]:
                break

    else: # Only check if not discarded
        if stack: # There are elements remining => unclosed sequence
            for opening in reversed(stack):
                local_score *= 5
                local_score += scores[opening]

            total_scores.append(local_score)

print(f"SOLUTION <{median(total_scores)}>")