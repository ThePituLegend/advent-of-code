def get_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [list(map(int, line.strip())) for line in f.readlines()]