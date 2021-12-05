def get_input(filename="input.txt"):
    with open(filename, "r") as f:
        nums = f.readline().strip().split(",")
        f.readline() # OOF but ok
        boards = [[row.split() for row in board.splitlines()] for board in f.read().split("\n\n")]

        return nums, boards

nums, boards = get_input("example.txt")