#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

t_l, b_r = get_input()

# ------------------ #

def test_probe(velocity):
    vel = velocity.copy()

    max_y = 0
    pos = {"x": 0, "y": 0}

    while pos["x"] < b_r["x"] and pos["y"] > b_r["y"]:
        pos["x"] += vel["x"]
        pos["y"] += vel["y"]

        max_y = max(max_y, pos["y"])

        if t_l["x"] <= pos["x"] <= b_r["x"] and t_l["y"] <= pos["y"] <= b_r["y"]:
            return max_y

        if vel["x"] != 0: 
            vel["x"] += 1 if vel["x"] < 0 else -1
        
        vel["y"] -= 1
    
    return False

biggest_y = 0

# Test some arbitrary number of trajectories: 0 <= x <= 400, -200 <= y <= 200
for x in range(401):
    for y in range(-200, 201):
        velocity = {"x" : x, "y": y}
        max_y = test_probe(velocity)

        if max_y:
            biggest_y = max(biggest_y, max_y)


print(f"SOLUTION <{biggest_y}>")