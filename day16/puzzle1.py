#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from packet import Packet
from get_input import get_input

packets = get_input()

# ------------------ #

def process_type4(packet_str):
    literal = ""
    i = 6
    nxt = int(packet_str[i])
    while nxt:
        literal += packet_str[i+1:i+5]
        i += 5
        nxt = int(packet_str[i])

    literal += packet_str[i+1:i+5]

    return int(literal, 2), i+5

def process_packet(packet_str, i=0):
    p = Packet(int(packet_str[:3], 2), int(packet_str[3:6], 2))

    if p.packet_type == 4:
        p.value, i = process_type4(packet_str)

    else:
        p.length_type = int(packet_str[6],)

        if p.length_type == 0:
            p.length = int(packet_str[7:22], 2)
            
            i = 22
            while i < (22 + p.length):
                operand, off = process_packet(packet_str[i:], i)
                i += off
                p.operands.append(operand)

        else:
            p.length = int(packet_str[7:18], 2)
            
            i = 18
            for _ in range(p.length):
                operand, off = process_packet(packet_str[i:], i)
                i += off
                p.operands.append(operand)

    versions.append(p.version)
    return p, i

versions = []
for packet_str in packets:
    versions = []
    p, i = process_packet(packet_str)
    print(f"SOLUTION <{sum(versions)}>")