def get_input():
    with open("input.txt", "r") as f:
        return [(c.split()[0], int(c.split()[1])) for c in f.read().splitlines()]