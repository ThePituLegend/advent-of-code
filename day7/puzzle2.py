#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from Tree import Tree
output = get_input()

fs = Tree()

for line in output:
    if line[0] == "$": # It's a cd, get folder
        folder = line.split()[-1]
        if folder == "..":
            fs.go_up()
        else:
            fs.add_node(folder)
    else: # It's an ls output, get name and size
        size, name = line.split()
        if size != "dir":
            fs.add_node(name, int(size))

fs.update_sizes()

unused_space = 70000000 - fs.root.size; missing_space = 30000000 - unused_space
print(min(filter(lambda x: x >= missing_space, fs.dirs)))