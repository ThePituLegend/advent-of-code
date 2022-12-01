#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

input = get_input()
print(sum(sorted(map(sum, input))[-3:]))