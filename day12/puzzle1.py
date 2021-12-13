#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from get_input import get_input

graph = get_input()

# ------------------ #

count = 0

def pathsRec(here, dest, visited, path):
    global count

    if here.islower():
        visited[here] = True

    path.append(here)

    if here == dest:
        print(",".join(path))
        count += 1   

    else:
        for i in list(filter(lambda x: visited[x] == False, graph[here])):
            pathsRec(i, dest, visited, path)
                    
    path.pop()
    visited[here] = False


visited = defaultdict(bool)
path = []
pathsRec("start", "end", visited, path)

print(f"SOLUTION <{count}>")