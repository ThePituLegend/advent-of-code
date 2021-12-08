#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
input = get_input()

# ------------------ #

LUT = { # Num. of seg: rendered number
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

total = 0

for line in input:
    patterns, output = line

    mapping = {}
    reverse_map = {}
    five = []
    six = []

    for pattern in patterns:
        ln = len(pattern)
        pat_set = frozenset(pattern)
        if ln in LUT:
            mapping[pat_set] = LUT[ln]
            reverse_map[LUT[ln]] = pat_set
            #print(f"Mapped {''.join(pat_set)} to {mapping[pat_set]}")
        elif ln == 5:
            five.append(pat_set)
        else:
            six.append(pat_set)
        

        
    for pat in six:
        if not pat.issuperset(reverse_map[1]):
            mapping[pat] = 6
            #print(f"Mapped {''.join(pat)} to {6}")
        elif not pat.issuperset(reverse_map[4]):
            mapping[pat] = 0
            #print(f"Mapped {''.join(pat)} to {0}")
        else:
            mapping[pat] = 9
            reverse_map[9] = pat
            #print(f"Mapped {''.join(pat)} to {9}")
    
    for pat in five:
        if pat.issuperset(reverse_map[1]):
            mapping[pat] = 3
            #print(f"Mapped {''.join(pat)} to {3}")
        elif pat.issubset(reverse_map[9]):
            mapping[pat] = 5
            #print(f"Mapped {''.join(pat)} to {5}")
        else:
            mapping[pat] = 2
            #print(f"Mapped {''.join(pat)} to {2}")


    num = int("".join(str(mapping[digit]) for digit in map(frozenset, output)))
    #print(f"{output}: {num}")

    total += num

    #print()

print(f"SOLUTION <{total}>")