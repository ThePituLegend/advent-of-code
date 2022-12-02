#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

round_value = {
    "A" : { # Rock
        "X" : 3, # lose = scissors
        "Y" : 4, # draw = rock
        "Z" : 8  # win = paper
    },
    "B" : { # Paper
        "X" : 1, # lose = rock
        "Y" : 5, # draw = paper
        "Z" : 9  # win = scissors
    },
    "C" : { # Scissors
        "X" : 2, # lose = paper
        "Y" : 6, # draw = scissors
        "Z" : 7  # win = rock
    }
}

rounds = get_input()
print(sum(map(lambda x: round_value[x[0]][x[1]], rounds)))