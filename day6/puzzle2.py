#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

stream = get_input()

win_size = 14

for i in range(len(stream) - win_size + 1):
    window = stream[i:i+win_size]
    if len(set(window)) == win_size:
        print(i+win_size)
        break