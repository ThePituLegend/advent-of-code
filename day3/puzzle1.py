#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input_1
from string import ascii_letters as letters

lines = get_input_1()

error = map(lambda x: x[0] & x[1], lines)
priorities = map(lambda x: letters.index(x.pop()) + 1, error)
print(sum(priorities))