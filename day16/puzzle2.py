#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from packet import Packet
from math import prod
from get_input import get_input

packets = get_input()

# ------------------ #

op = {
    0 : sum,
    1 : prod,
    2 : min, 
    3 : max,

    5 : lambda x, y: 1 if x > y else 0,
    6 : lambda x, y: 1 if x < y else 0,
    7 : lambda x, y: 1 if x == y else 0
}

def eval_packet(p: Packet):
    if p.packet_type == 4:
        return p.value
    
    operands = [eval_packet(pckt) for pckt in p.operands]
    if p.packet_type < 4:
        return op[p.packet_type](operands)
    else:
        return op[p.packet_type](*operands)
    
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

    return p, i

for packet_str in packets:
    p, i = process_packet(packet_str)
    res = eval_packet(p)

    print(f"SOLUTION <{res}>")