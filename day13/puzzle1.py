#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from itertools import zip_longest

packets = get_input()

def compare(left, right):
    print(f"Comparing {left} and {right}")

    if type(left) == int and type(right) == int: # Both are ints
        if left == right:
            return "keep"

        return left < right

    elif type(left) == list and type(right) == list: # Both are lists
        for pair in zip_longest(left, right):

            if [] in pair:
                print("WARNING; Empty list")

            correct = compare(pair[0], pair[1])

            if correct != "keep":
                return correct

    else: # Mixed types
        if left in [None, []] and right in [None, []]:
            return True
        elif left == None and right not in [None, []]:
            return True
        elif right == None and left not in [None, []]:
            return False

        print("Mixed types, retry")
        left = [left] if type(left) == int else left
        right = [right] if type(right) == int else right
        return compare(left, right)

    return True


indices = []
for i, pair in enumerate(packets, 1):
    correct = compare(pair[0], pair[1])
    if correct:
        print(f"Packet {i} is correct")
        indices.append(i)
    else:
        print(f"Packet {i} is incorrect")
    print()

print(indices)
print(sum(indices))