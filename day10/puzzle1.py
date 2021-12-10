#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

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
    "}": 1197,
    ")": 3,
    "]": 57,
    ">": 25137
}

total_score = 0
for line in input:
    stack = []
    
    for char in line:
        if char in push_char:
            stack.append(char)
        else:
            opening = stack.pop()
            if char != pop_char[opening]:
                #print(f"- {''.join(line)} - Expected {pop_char[opening]}, but found {char} instead.")
                total_score += scores[char]
                break

print(f"SOLUTION <{total_score}>")