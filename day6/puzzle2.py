#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from collections import deque

fishes = get_input()

# ------------------ #

timers = deque([0] * 10)
for fish in fishes:
    timers[fish] += 1

for day in range(256):
    news = timers[0]
    
    timers.rotate(-1)
    timers[-1] = 0 # Clears the "rotation element"
    
    timers[6] += news
    timers[8] = news
  
print(f"There are a total of {sum(timers)} fish")