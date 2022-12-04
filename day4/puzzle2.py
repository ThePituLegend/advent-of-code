#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

pairs = get_input()
print(sum(map(lambda x: not x[0].isdisjoint(x[1]), pairs)))