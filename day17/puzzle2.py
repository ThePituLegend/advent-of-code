#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

t_l, b_r = get_input("example.txt")

# ------------------ #

def test_probe(velocity):
    vel = velocity.copy()

    pos = {"x": 0, "y": 0}

    while pos["x"] < b_r["x"] and pos["y"] > b_r["y"]:
        pos["x"] += vel["x"]
        pos["y"] += vel["y"]

        if t_l["x"] <= pos["x"] <= b_r["x"] and t_l["y"] <= pos["y"] <= b_r["y"]:
            return True

        if vel["x"] != 0: 
            vel["x"] += 1 if vel["x"] < 0 else -1
        
        vel["y"] -= 1
    
    return False

valid_shots = 0

# Test some arbitrary number of trajectories: 0 <= x <= ?, ? <= y <= ?
for x in range(50):
    for y in range(-20, 21):
        velocity = {"x" : x, "y": y}
        valid = test_probe(velocity)

        if valid:
            valid_shots += 1
            print(f"{velocity['x']}, {velocity['y']}")

print(f"SOLUTION <{valid_shots}>")