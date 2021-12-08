def get_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [[x.split() for x in line.split("|")] for line in f.readlines()]