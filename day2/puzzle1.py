#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

input = get_input()

# ------------------ #

def forward(pos, n):
    pos[0] += n

def down(pos, n):
    pos[1] += n

def up(pos, n):
    pos[1] -= n

commands = {
    "forward" : forward,
    "down" : down,
    "up" : up
}


pos = [0, 0]

for step in input:
    commands[step[0]](pos, step[1])

print(f"Final position => ({pos[0]}, {pos[1]})")
print(f"SOLUTION <{pos[0]*pos[1]}>")