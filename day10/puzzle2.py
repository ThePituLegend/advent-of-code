#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input
from Cpu import CPU

cpu = CPU(crt=True)
cpu.ram = get_input()
cpu.run()