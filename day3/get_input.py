def get_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [[int(d) for d in number] for number in f.read().splitlines()]
