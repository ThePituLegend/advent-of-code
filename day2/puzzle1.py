#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

round_value = {
    "A" : { # Rock
        "X" : 4, # Rock vs Rock = draw
        "Y" : 8, # Paper vs Rock = win
        "Z" : 3  # Scissors vs Rock = lose
    },
    "B" : { # Paper
        "X" : 1, # Rock vs Paper = lose
        "Y" : 5, # Paper vs Paper = draw
        "Z" : 9  # Scissors vs Paper = win
    },
    "C" : { # Scissors
        "X" : 7, # Rock vs Scissors = win
        "Y" : 2, # Paper vs Scissors = lose
        "Z" : 6  # Scissors vs Scissors = draw
    }
}

rounds = get_input()
print(sum(map(lambda x: round_value[x[0]][x[1]], rounds)))