#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_input import get_input

nums, boards = get_input()

boards = [[[[n,  False] for n in row] for row in board] for board in boards] # Add mark field

# ------------------ #

# Step 1: Marking
for num in nums:
    for i, board in enumerate(boards):
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell[0] == num:
                    cell[1] = True

                    # Step 2: Check winning
                    if all(c[1] for c in row) or all(board[y_tmp][x][1] for y_tmp in range(5)): # Winning row
                        print(f"Board {i} won with number {num}")

                        # Step 3: Score
                        unmarked = sum(int(c[0]) for r in board for c in r if not c[1])
                        score = unmarked * int(num)

                        print(f"SOLUTION <{score}>")
                        exit()