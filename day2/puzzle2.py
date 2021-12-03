#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

input = get_input()

# ------------------ #

def forward(pos, aim, n):
    pos[0] += n
    pos[1] += aim[0]*n

def down(_, aim, n):
    aim[0] += n

def up(_, aim, n):
    aim[0] -= n

commands = {
    "forward" : forward,
    "down" : down,
    "up" : up
}

pos = [0, 0]
aim = [0]

for step in input:
    commands[step[0]](pos, aim, step[1])

print(f"Final position => ({pos[0]}, {pos[1]})")
print(f"Final aim => {aim}")
print(f"SOLUTION <{pos[0]*pos[1]}>")