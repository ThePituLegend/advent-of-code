def get_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [int(n) for n in f.read().split(",")]
