#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input_2
from string import ascii_letters as letters

groups = get_input_2()

badge = map(lambda x: x[0] & x[1] & x[2], groups)
priorities = map(lambda x: letters.index(x.pop()) + 1, badge)
print(sum(priorities))