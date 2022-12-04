#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

pairs = get_input()
print(sum(map(lambda x: x[0] >= x[1] or x[1] >= x[0], pairs)))